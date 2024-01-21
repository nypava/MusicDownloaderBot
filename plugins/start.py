from pyrogram.client import Client as app
from pyrogram import filters
from utilities.buttons.button import start_btn
import json

with open("utilities/text/text.json", "r", encoding="utf-8") as json_data:
    data = json.load(json_data)

@app.on_message(filters.command("start"))
async def start(client, message):
    first_name = message.from_user.first_name

    await message.reply(data["start"].format(first_name), reply_markup=start_btn)
