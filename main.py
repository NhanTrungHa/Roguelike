import tcod

from Engine import Engine
from input_handlers import EventHandler
from entity import Entity
from procgen import generate_dungeon
import copy
import entity_factories

def main() -> None:
    screen_width = 160
    screen_height = 90

    player = copy.deepcopy(entity_factories.player)

    engine = Engine(player=player)


    map_width = 160
    map_height = 90

    room_max_size = 10
    room_min_size = 6
    max_rooms = 30

    max_monsters_per_room=2

    tileset = tcod.tileset.load_tilesheet("dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD)

    event_handler = EventHandler(engine)

    player = copy.deepcopy(entity_factories.player)

    engine.game_map = generate_dungeon(
        max_rooms=max_rooms,
        room_min_size=room_min_size,
        room_max_size=room_max_size,
        map_width=map_width,
        map_height=map_height,
        max_monsters_per_room=max_monsters_per_room,
        engine=engine,
    )
    engine.update_fov()

    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title="Nhan's Perilous Dungeon",
        vsync=True
    ) as context:
        root_console = tcod.Console(screen_width, screen_height, order="F")
        while True:
            engine.render(console=root_console, context=context)

            engine.event_handler.handle_events()




if __name__ == "__main__":
    main()