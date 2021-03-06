from __future__ import annotations

from typing import Iterable, TYPE_CHECKING, Optional

import numpy as np
from tcod.console import Console

import tile_types

if TYPE_CHECKING:
    from entity import Entity
    from engine import Engine


class GameMap:
    def __init__(
            self, engine: Engine, width: int, height: int, entities: Iterable[Entity] = ()
    ):
        self.engine = engine
        self.width, self.height = width, height
        self.entities = set(entities)
        self.tiles = np.full((width, height), fill_value=tile_types.wall, order="F")
        self.visible = np.full(
            (width, height), fill_value=False, order="F"
        )  # Tiles that are currently visible
        self.explored = np.full(
            (width, height), fill_value=False, order="F"
        )  # Tiles that have been previously seem

    def get_blocking_entity_at_location(
            self, location_x: int, location_y: int
    ) -> Optional:
        for entity in self.entities:
            if (
                    entity.blocks_movement
                    and entity.x == location_x
                    and entity.y == location_y
            ):
                return entity

        return None

    def in_bounds(self, x: int, y: int) -> bool:
        """Return true of x and y are inside bounds of the map"""
        return 0 <= x < self.width and 0 <= y < self.height

    def render(self, console: Console) -> None:
        """
        Renders the map

        If tile is in "visible", draw with "light"
        If it isn't but it's in "explored", draw with "dark"
        Otherwise "SHROUD"

        """
        console.tiles_rgb[0: self.width, 0: self.height] = np.select(
            condlist=[self.visible, self.explored],
            choicelist=[self.tiles["light"], self.tiles["dark"]],
            default=tile_types.SHROUD,
        )

        for entity in self.entities:
            # only print entities in FOV
            if self.visible[entity.x, entity.y]:
                console.print(entity.x, entity.y, entity.char, fg=entity.color)
