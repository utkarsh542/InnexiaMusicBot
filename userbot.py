# import logging
from pyrogram import Client, idle

app = Client("MMB")
# logging.basicConfig(level=logging.INFO)
app.start()
print('>>> MAFIA MUSIC BOT STARTED')
idle()
app.stop()
print('\n>>> MAFIA MUSIC BOT STOPPED')
