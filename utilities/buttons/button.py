from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_btn = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("Channel",url="https://t.me/neuralp"),
        InlineKeyboardButton("Group",url="https://t.me/neuralg"),
    ],
    [
        InlineKeyboardButton("📁 Source code",url="https://github.com/NYDEV0/SpeechRecognitionBot"),
    ]
])
