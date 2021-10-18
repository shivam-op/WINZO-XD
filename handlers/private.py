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
        f"""**Hey there! My name is ƵɆ¥ɌØӾ.✨
I can play music in your group🎉 .
Add me in your group and play music freely.🇮🇳**
Our chatting group:- @Friends_Forever_143
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🙋‍♂ Devlopers", url="https://t.me/Shivam9412")
                  ],[
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/ELECTRO_UPDATES"
                    ),
                    InlineKeyboardButton(
                        "💬 Support", url="https://t.me/electrobot_support"
                    )    
                ],[ 
                    InlineKeyboardButton(
                        "➕ Add me to group ➕", url="https://t.me/{bn}?startgroup=true"
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
