from pyrogram.client import Client as app
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from utilities.helpers.finder import Youtube

@app.on_message(filters.text)
async def main(client, message):
    chat_id = message.chat.id

    yt = Youtube(message.text)

    image = yt.image()
    videos = yt.videos()

    inline_buttons = []   
    for video in videos:
        inline_buttons.append([InlineKeyboardButton(f"🎵 {video[2]} ・ {video[1]} ", callback_data=video[0])])
    
    await client.send_photo(chat_id=chat_id,caption="__choose the music:__", photo=image, reply_markup=InlineKeyboardMarkup(inline_buttons))
