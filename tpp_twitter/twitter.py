from dotenv import load_dotenv
import tweepy
from os import getenv
from typing import BinaryIO

BASE_BIO = "Inspired by @screenshakes. Powered by PyBoy: http://github.com/Baekalfen/PyBoy\n"

load_dotenv()

auth = tweepy.OAuthHandler(getenv('TWITTER_KEY'), getenv('TWITTER_SECRET'))
auth.set_access_token(getenv('TWITTER_ACCESS'), getenv('TWITTER_ACCESS_TOKEN'))

api = tweepy.API(auth)

def get_replies_from_latest():
    """Gathers replies from latest Tweet in order of popularity."""
    latest_status = api.user_timeline(count=1, exclude_replies=True)[0]
    return tweepy.Cursor(api.search, q="to:TextOnlyGameBoy", since_id=latest_status.id, result_type="recent").items()

def update(tweet_image: BinaryIO, profile_image: BinaryIO, text: str = "Image", bio: str = ""):
    """Send a Tweet with an image and optionally update the bio."""
    screenshot = api.media_upload("screenshot.jpg", file=tweet_image)
    api.update_profile_image("screenshot.jpg", file_=profile_image)
    api.update_status(text, media_ids=[screenshot.media_id])
    if bio:
        api.update_profile(description=BASE_BIO + bio)
