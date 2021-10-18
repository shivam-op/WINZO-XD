from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME, BOT_USERNAME
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
     await message.reply_text(
        f"""**𝐇𝐞𝐲,𝐈 𝐚𝐦 𝐙𝐞𝐲𝐫𝐨𝐱
𝐈 𝐚𝐦 𝐚𝐧 𝐚𝐝𝐯𝐚𝐧𝐜𝐞𝐝 𝐦𝐮𝐬𝐢𝐜 𝐛𝐨𝐭 𝐚𝐧𝐝 𝐢 𝐜𝐚𝐧 𝐩𝐥𝐚𝐲 𝐦𝐮𝐬𝐢𝐜 𝐢𝐧 𝐠𝐫𝐨𝐮𝐩 𝐯𝐨𝐢𝐜𝐞 𝐜𝐡𝐚𝐭.
𝐈𝐟 𝐲𝐩𝐮 𝐧𝐞𝐞𝐝 𝐚𝐧𝐲 𝐡𝐞𝐥𝐩 𝐤𝐢𝐧𝐝𝐥𝐲 𝐜𝐨𝐧𝐭𝐚𝐜𝐭 𝐮𝐬 𝐚𝐭 𝐨𝐮𝐫 𝐬𝐮𝐩𝐩𝐨𝐫𝐭 𝐠𝐫𝐨𝐮𝐩**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝐆𝐫𝐨𝐮𝐩", url="https://t.me/ELECTROBOT_SUPPORT")
                  ],[
                    InlineKeyboardButton(
                        "𝐂𝐡𝐚𝐧𝐧𝐞𝐥", url="https://t.me/ELECTRO_UPDATES"
                    ),
                    InlineKeyboardButton(
                        "𝐁𝐨𝐭 𝐥𝐢𝐬𝐭", url="https://t.me/bondofbestizz"
                    )    
                ],[ 
                    InlineKeyboardButton(
                        "𝐀𝐝𝐝 𝐦𝐞 𝐭𝐨 𝐠𝐫𝐨𝐮𝐩", url="https://t.me/{BOT_USERNAME}?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Yes iᴍ online ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝐂𝐇𝐀𝐍𝐍𝐄𝐋", url="https://t.me/ELECTRO_UPDATES")
                ]
            ]
        )
   )
