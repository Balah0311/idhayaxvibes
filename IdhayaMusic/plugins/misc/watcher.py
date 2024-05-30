from pyrogram import filters
from pyrogram.types import Message

from IdhayaMusic import app
from IdhayaMusic.core.call import Idhaya

welcome = 20
close = 30


@app.on_message(filters.video_chat_started, group=welcome)
@app.on_message(filters.video_chat_ended, group=close)
async def welcome(_, message: Message):
    await Idhaya.stop_stream_force(message.chat.id)
