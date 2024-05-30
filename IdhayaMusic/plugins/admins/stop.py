from pyrogram import filters
from pyrogram.types import Message

from IdhayaMusic import app
from IdhayaMusic.core.call import Inflex
from IdhayaMusic.utils.database import set_loop
from IdhayaMusic.utils.decorators import AdminRightsCheck
from IdhayaMusic.utils.inline import close_markup
from config import BANNED_USERS


@app.on_message(
    filters.command(["end", "stop", "cend", "cstop"]) & filters.group & ~BANNED_USERS
)
@AdminRightsCheck
async def stop_music(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return
    await Idhaya.stop_stream(chat_id)
    await set_loop(chat_id, 0)
    await message.reply_text(
        _["admin_5"].format(message.from_user.mention), reply_markup=close_markup(_)
    )
