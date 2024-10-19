from DUGGUMUSIC.core.bot import Aviax
from DUGGUMUSIC.core.dir import dirr
from DUGGUMUSIC.core.git import git
from DUGGUMUSIC.core.userbot import Userbot
from DUGGUMUSIC.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Aviax()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
