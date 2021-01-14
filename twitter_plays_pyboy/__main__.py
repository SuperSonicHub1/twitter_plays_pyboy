from pyboy import PyBoy, WindowEvent
from PIL import Image
from typing import List
from .constants import BUTTON_INPUTS


filename = "test_rom.gb"

# Initialize emulator
emu = PyBoy(filename, window_type="headless", window_scale=3, debug=False, game_wrapper=True)
emu.set_emulation_speed(0)

mario = emu.game_wrapper()
mario.start_game()

# Used for numbering screenshots
n = 0
while True:
    n+=1

    # Get window events
    inputs: List[WindowEvent] = []
    button = input("> ").lower()
    if button == "q":
        emu.stop()
        exit(0)
    else:
        inputs = BUTTON_INPUTS.get(button, [])
        if not inputs:
            continue
    press, release = inputs
    
    # Press button for three frames
    emu.send_input(press)
    for _ in range(3):
        emu.tick()
    emu.send_input(release)

    # Get screenshot
    with emu.botsupport_manager().screen().screen_image() as screenshot:
        screenshot.save(f"test_images/{1}.jpg", "JPEG")
