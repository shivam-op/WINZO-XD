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
        f"""**Hey there! I am a part of Electro.✨
I can play music in your group🎉 .
Add me in your group and play music freely.🇮🇳**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚡️ Winzo Official", url="https://t.me/WINZOGOLD7773")
                  ],[
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/ELECTRO_UPDATES"
                    ),
                    InlineKeyboardButton(
                        "💬 Support", url="https://t.me/electrobot_support"
                    )    
                ],[ 
                    InlineKeyboardButton(
                        "➕ Add me to group ➕", url="https://t.me/WINZOMUSICBOT?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**𝐇𝐄𝐘, 𝐃𝐔𝐃𝐄 𝐈 𝐀𝐌 𝐀𝐋𝐈𝐕𝐄✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝐂𝐇𝐀𝐍𝐍𝐄𝐋", url="https://t.me/ELECTRO_UPDATES")
                ]
            ]
        )
   )
