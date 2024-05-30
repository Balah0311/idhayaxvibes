from IdhayaMusic.core.bot import Inflex
from IdhayaMusic.core.dir import dirr
from IdhayaMusic.core.git import git
from IdhayaMusic.core.userbot import Userbot
from IdhayaMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Inflex()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
