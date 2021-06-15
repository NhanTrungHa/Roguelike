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
        ("walkable", np.bool), # True if tile is able to be walked over
        ("transparent", np.bool), # True if tile doesn't block FOV.
        ("dark", graphic_dt), # Graphics for when tile is not in FOV

    ]
)

def new_tile(
        *, # enforces keyword use
        walkable: int,
        transparent: int,
        dark: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
) -> np.ndarray:
    return np.array((walkable, transparent, dark), dtype=tile_dt)

floor = new_tile(
    walkable=True, transparent=True, dark=(ord(" "), (255, 255, 255), (50, 50, 150))
)
wall = new_tile(
    walkable=False, transparent=False, dark=(ord(" "), (255, 255, 255), (0, 0, 100))
)