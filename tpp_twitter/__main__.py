from PIL import Image
from pyboy import PyBoy, WindowEvent
import schedule
from argparse import ArgumentParser
from io import BytesIO
import time
from typing import List
import twitter_plays_pyboy
import tpp_twitter as twitter

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

def job():
    for status in twitter.get_replies_from_latest():
        button = status.text.split(" | ", 1)[0]
        inputs = twitter_plays_pyboy.constants.BUTTON_INPUTS.get(button, [])
        if not inputs:
            continue
        press, release = inputs
        game.input(press, release)
    else:
        inputs = twitter_plays_pyboy.constants.BUTTON_INPUTS['pass']
        press, release = inputs
        game.input(press, release)

    with game.screenshot() as screenshot:
        screenshot_bin = BytesIO()
        screenshot.save(screenshot_bin, "JPEG")
    
    twitter.update(screenshot_bin, BytesIO(screenshot_bin.getvalue()), text="", bio=game.bio())

schedule.every(30).seconds.do(job)

while True:
    try:
        schedule.run_pending()
        time.sleep(1)
    except KeyboardInterrupt:
        game.emu.stop()
        exit(0)

