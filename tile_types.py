from typing import Tuple

import numpy as np

# Tile graphics structured type compatible with Console.tiles_rgb
graphic_dt = np.dtype(
    [
        ("ch", np.int32),
        ("fg", "3B"),
        ("bg", "3B")
    ]
)

tile_dt = np.dtype(
    [
        ("walkable", np.bool),  # True if tile is able to be walked over
        ("transparent", np.bool),  # True if tile doesn't block FOV.
        ("dark", graphic_dt),  # Graphics for when tile is not in FOV
        ("light", graphic_dt),
    ]
)


def new_tile(
        *,  # enforces keyword use
        walkable: int,
        transparent: int,
        dark: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
        light: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
) -> np.ndarray:
    return np.array((walkable, transparent, dark, light), dtype=tile_dt)


# unseen, unexplored tiles
SHROUD = np.array((ord(" "), (255, 255, 255), (0, 0, 0)), dtype=graphic_dt)

floor = new_tile(
    walkable=True,
    transparent=True,
    dark=(ord("."), (120, 120, 120), (0, 0, 0)),
    light=(ord("."), (255, 255, 255), (0, 0, 0))
)
wall = new_tile(
    walkable=False,
    transparent=False,
    dark=(ord("#"), (0, 0, 0), (120, 120, 120)),
    light=(ord("#"), (0, 0, 0), (171, 247, 255))
)
