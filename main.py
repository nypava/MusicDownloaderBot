from pyrogram.client import Client
from config import bot_token, api_hash, api_id
 
app = Client(name="session", bot_token=bot_token, api_hash=api_hash, api_id=api_id, plugins={"root":"plugins", "include":["start", "callback", "main"]})

app.run()
