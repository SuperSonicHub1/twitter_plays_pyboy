from pyboy import PyBoy, WindowEvent
from PIL import Image
from argparse import ArgumentParser
from typing import List
import twitter_plays_pyboy

parser = ArgumentParser(
    prog="Twitter Plays Game Boy",
    description="A clone of Constantin Liétard's 'Twitter Plays Pokémon' (https://nitter.net/screenshakes/status/1347589296593788933). Powered by PyBoy (https://github.com/Baekalfen/PyBoy)."
)
parser.add_argument('filename', help="Location of ROM.")
parser.add_argument('-g', '--game', help="Game class used. If you're unsure what to use, pick `BaseGame`.", default="BaseGame", choices=twitter_plays_pyboy.games.__all__)
parser.add_argument('-V', '--version', action='version', version='%(prog)s ' + twitter_plays_pyboy.__version__)


args = parser.parse_args()

engine = getattr(twitter_plays_pyboy.games, args.game)

# Initialize emulator
emu = PyBoy(args.filename, window_type="headless", debug=False, game_wrapper=True)
emu.set_emulation_speed(0)

game = engine(emu)

last_bio = ""
while True:
    # Get window events
    inputs: List[WindowEvent] = []
    button = input("> ").lower()
    if button == "q":
        emu.stop()
        exit(0)
    else:
        inputs = twitter_plays_pyboy.constants.BUTTON_INPUTS.get(button, [])
        if not inputs:
            continue
    press, release = inputs
    
    # Send input
    game.input(press, release)

    if last_bio == game.bio():
        pass
    else:
        last_bio = game.bio()
        print(last_bio)

    # Get screenshot
    with game.screenshot() as screenshot:
        screenshot.save(f"test_images/{1}.jpg", "JPEG")
