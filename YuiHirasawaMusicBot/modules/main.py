from pyrogram import Client, idle

from YuiHirasawaMusicBot.config import API_ID, API_HASH, BOT_TOKEN
from YuiHirasawaMusicBot.modules.videoplayer import app

bot = Client(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="bot"),
)

bot.start()
app.start()
idle()
