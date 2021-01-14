from pyboy import PyBoy, WindowEvent
from PIL import Image
from typing import Optional


class BaseGame:
    emulator: PyBoy
    def __init__(self, emulator: PyBoy):
        """Initialize the emulator."""
        self.emu = emulator
    def bio(self) -> str:
        """What to leave in the Twitter bio along with the standard stuff after the screen updates."""
        return f'Playing {self.emu.cartridge_title()}.'
    def input(self, press: Optional[WindowEvent], release: Optional[WindowEvent]):
        """Send input to emulator."""
        if not press or not release:
            pass
        else:
            self.emu.send_input(press)
        
        for _ in range(3):
            self.emu.tick()
        
        if not press or not release:
            pass
        else:
            self.emu.send_input(release)
    def screenshot(self) -> Image:
        """Return a screenshot."""
        return self.emu.botsupport_manager().screen().screen_image()