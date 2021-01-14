from pyboy import PyBoy, WindowEvent
from pyboy.plugins.game_wrapper_super_mario_land import GameWrapperSuperMarioLand
from PIL import Image
from typing import Optional
from .base import BaseGame


class SuperMarioLand(BaseGame):
    mario: GameWrapperSuperMarioLand
    def __init__(self, emulator: PyBoy):
        """Initialize the emulator."""
        super().__init__(emulator)
        self.mario = self.emu.game_wrapper()
        self.mario.start_game()
    def bio(self) -> str:
        """What to leave in the Twitter bio along with the standard stuff after the screen updates."""
        world, stage = self.mario.world
        return f"""Playing Super Mario Land
World {world}-{stage}
Score: {self.mario.score}
Coins: {self.mario.coins}
Lives: {self.mario.lives_left}
Time: {self.mario.time_left}"""