from __future__ import annotations
from typing import Optional, TYPE_CHECKING

import tcod.event

from actions import Action, EscapeAction, MovementAction, BumpAction

if TYPE_CHECKING:
    from engine import Engine

class EventHandler(tcod.event.EventDispatch[Action]):
    def __init__(self, engine: Engine):
        self.engine = engine

    def handle_events(self) -> None:

        for event in tcod.event.wait():
            action = self.dispatch(event)

            if action is None:
                continue

            action.perform()
            self.engine.handle_enemy_turns()
            self.engine.update_fov()  # update fov before next player action

    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
        raise SystemExit()

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
        action: Optional[Action] = None

        key = event.sym

        player = self.engine.player

        if key == tcod.event.K_k:
            action = BumpAction(player, dx=0, dy=-1)
        elif key == tcod.event.K_j:
            action = BumpAction(player, dx=0, dy=1)
        elif key == tcod.event.K_h:
            action = BumpAction(player, dx=-1, dy=0)
        elif key == tcod.event.K_l:
            action = BumpAction(player, dx=1, dy=0)
        elif key == tcod.event.K_u:
            action = BumpAction(player, dx=1, dy=-1)
        elif key == tcod.event.K_y:
            action = BumpAction(player, dx=-1, dy=-1)
        elif key == tcod.event.K_b:
            action = BumpAction(player, dx=-1, dy=1)
        elif key == tcod.event.K_n:
            action = BumpAction(player, dx=1, dy=1)
        elif key == tcod.event.K_ESCAPE:
            action = EscapeAction(player)

        return action
