from typing import Iterable, Any

from tcod.context import Context
from tcod.console import Console
from tcod.map import compute_fov

from actions import EscapeAction, MovementAction
from entity import Entity
from input_handlers import EventHandler
from game_map import GameMap

class Engine:
    def __init__(self, event_handler: EventHandler, game_map: GameMap, player: Entity):
        self.event_handler = event_handler
        self.player = player
        self.game_map = game_map
        self.update_fov()

    def handle_enemy_turns(self) -> None:
        for entity in self.game_map.entities - {self.player}:
            print(f'The {entity.name} wonders when it will get to take a real turn.')



    def update_fov(self) -> None:
        """ Recompute visible area based on player FOV """
        self.game_map.visible[:] = compute_fov(
            self.game_map.tiles["transparent"],
            (self.player.x, self.player.y),
            radius=8,
        )
        # if a tile is "visible", add to "explored"
        self.game_map.explored |= self.game_map.visible

    def render(self, console: Console, context: Context) -> None:
        self.game_map.render(console)


        context.present(console)

        console.clear()