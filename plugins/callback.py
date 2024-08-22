from pyrogram.client import Client as app
from utilities.helpers.finder import nameFinder
from utilities.helpers.downloader import download 
from threading import Thread
import json
import os

with open("utilities/text/text.json", "r", encoding="utf-8") as json_data:
    data = json.load(json_data)


def main(client, callbackquery):
    chat_id = callbackquery.message.chat.id
    query = callbackquery.data

    callbackquery.answer()

    callbackquery.message.delete()

    title = nameFinder(query)

    download_msg = data["download"].format(title)
    download_dist = "" 

    status = client.send_message(chat_id, download_msg)
    
    try:
        download_dist = download(query)
    except Exception as error:
        client.send_message(chat_id=chat_id, text=error)

    upload_msg = data["upload"].format(title)
    status.edit_text(upload_msg)
    
    client.send_video(chat_id=chat_id, video=download_dist)
    status.delete()

    os.remove(download_dist)


@app.on_callback_query()
def callback(client, callbackquery):
    thread = Thread(target=main, args=[client, callbackquery])
    thread.start()
