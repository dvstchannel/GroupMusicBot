from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgUAAxkBAAP5YMFqSakH6Uy6WbJXvpbLqn5e6FUAAhgFAAL4xsUK3oW39ORkPRgfBA")
    await message.reply_text(
        f"""**Hey, Tôi là {bn} 🎵

Tôi có thể phát nhạc trong cuộc gọi thoại của nhóm bạn. Được phát triển bởi [Sabo](https://t.me/BotSabo).

Thêm tôi vào nhóm của bạn và chơi nhạc tự do!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/nanglive"
                    ),
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/kenhsex"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➕ Thêm tôi vào nhóm ➕", url="https://t.me/HiSabo_bot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Group Music Player trực tuyến ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/kenhsex")
                ]
            ]
        )
   )


