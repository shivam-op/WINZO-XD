from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def help_(client: Client, message: Message):
     await message.reply_text(
        f"""**Hey there! I am a part of Electro.â¨
I can play music in your groupð .
Add me in your group and play music freely.ð®ð³**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "â¡ï¸ Winzo Official", url="https://t.me/WINZOGOLD7773")
                  ],[
                    InlineKeyboardButton(
                        "ð Channel", url="https://t.me/ELECTRO_UPDATES"
                    ),
                    InlineKeyboardButton(
                        "ð¬ Support", url="https://t.me/electrobot_support"
                    )    
                ],[ 
                    InlineKeyboardButton(
                        "â Add me to group â", url="https://t.me/WINZOMUSICBOT?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**ððð, ðððð ð ðð ðððððâ**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ððððððð", url="https://t.me/ELECTRO_UPDATES")
                ]
            ]
        )
   )
