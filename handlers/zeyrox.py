from os import path
from typing import Dict
from pyrogram import Client
from pyrogram.types import Message, Voice
from typing import Callable, Coroutine, Dict, List, Tuple, Union
from callsmusic import callsmusic, queues
from helpers.admins import get_administrators
from os import path
import requests
import aiohttp
import yt_dlp
from youtube_search import YoutubeSearch
from pyrogram import filters, emoji
from pyrogram.types import InputMediaPhoto
from pyrogram.errors.exceptions.bad_request_400 import ChatAdminRequired
from pyrogram.errors.exceptions.flood_420 import FloodWait
import traceback
import os
import sys
from callsmusic.callsmusic import client as USER
from pyrogram.errors import UserAlreadyParticipant
import converter
from downloaders import youtube

from config import BOT_NAME as bn, DURATION_LIMIT
from helpers.filters import command, other_filters
from helpers.decorators import errors, authorized_users_only
from helpers.errors import DurationLimitError
from helpers.gets import get_url, get_file_name
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from cache.admins import admins as a
import os
import aiohttp
import aiofiles
import ffmpeg
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from config import que
from Python_ARQ import ARQ
import json
import wget
chat_id = None

           


def cb_admin_check(func: Callable) -> Callable:
    async def decorator(client, cb):
        admemes = a.get(cb.message.chat.id)
        if cb.from_user.id in admemes:
            return await func(client, cb)
        else:
            await cb.answer('You ain\'t allowed!', show_alert=True)
            return
    return decorator                                                                       
                                          
                                          
                                          
                                          
def transcode(filename):
    ffmpeg.input(filename).output("input.raw", format='s16le', acodec='pcm_s16le', ac=2, ar='48k').overwrite_output().run() 
    os.remove(filename)

# Convert seconds to mm:ss
def convert_seconds(seconds):
    seconds = seconds % (24 * 3600)
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return "%02d:%02d" % (minutes, seconds)


# Convert hh:mm:ss to seconds
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(':'))))


# Change image size
def changeImageSize(maxWidth, maxHeight, image):
    widthRatio = maxWidth / image.size[0]
    heightRatio = maxHeight / image.size[1]
    newWidth = int(widthRatio * image.size[0])
    newHeight = int(heightRatio * image.size[1])
    newImage = image.resize((newWidth, newHeight))
    return newImage

async def generate_cover(requested_by, title, views, duration, thumbnail):
    async with aiohttp.ClientSession() as session:
        async with session.get(thumbnail) as resp:
            if resp.status == 200:
                f = await aiofiles.open("background.png", mode="wb")
                await f.write(await resp.read())
                await f.close()

    image1 = Image.open("./background.png")
    image2 = Image.open("etc/foreground.png")
    image3 = changeImageSize(1280, 720, image1)
    image4 = changeImageSize(1280, 720, image2)
    image5 = image3.convert("RGBA")
    image6 = image4.convert("RGBA")
    Image.alpha_composite(image5, image6).save("temp.png")
    img = Image.open("temp.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("etc/font.otf", 32)
    draw.text((205, 550), f"Title: {title}", (51, 215, 255), font=font)
    draw.text(
        (205, 590), f"Duration: {duration}", (255, 255, 255), font=font
    )
    draw.text((205, 630), f"Views: {views}", (255, 255, 255), font=font)
    draw.text((205, 670),
        f"Added By: {requested_by}",
        (255, 255, 255),
        font=font,
    )
    img.save("final.png")
    os.remove("temp.png")
    os.remove("background.png")


@Client.on_message(command("playop") & other_filters)
async def play(_, message: Message):
    global que
    lel = await message.reply("🔄 **Processing**")
    administrators = await get_administrators(message.chat)
    chid = message.chat.id

    try:
        user = await USER.get_me()
    except:
        user.first_name =  "patriciaXmusic"
    usar = user
    wew = usar.id
    try:
        #chatdetails = await USER.get_chat(chid)
        lmoa = await _.get_chat_member(chid,wew)
    except:
           for administrator in administrators:
                      if administrator == message.from_user.id:  
                          try:
                              invitelink = await _.export_chat_invite_link(chid)
                          except:
                              await lel.edit(
                                  "<b>Add me as admin of yor group first</b>",
                              )
                              return

                          try:
                              await USER.join_chat(invitelink)
                              await USER.send_message(message.chat.id,"I joined this group for playing music in VC")
                              await lel.edit(
                                  "<b> userbot joined your chat</b>",
                              )

                          except UserAlreadyParticipant:
                              pass
                          except Exception as e:
                              #print(e)
                              await lel.edit(
                                  f"<b>🔴 Flood Wait Error 🔴 \nUser {user.first_name} couldn't join your group due to heavy requests for userbot! Make sure user is not banned in group."
                                  "\n\nOr manually add @patriciaXmusic to your Group and try again</b>",
                              )
                              pass
    try:
        chatdetails = await USER.get_chat(chid)
        #lmoa = await client.get_chat_member(chid,wew)
    except:
        await lel.edit(
            f"<i> @VCPlayRobot Userbot not in this chat, Ask admin to send /play command for first time or add assistant manually</i>"
        )
        return     
    sender_id = message.from_user.id
    sender_name = message.from_user.first_name
    await lel.edit("🔎 **Finding**")
    sender_id = message.from_user.id
    user_id = message.from_user.id
    sender_name = message.from_user.first_name
    user_name = message.from_user.first_name
    rpk = "["+user_name+"](tg://user?id="+str(user_id)+")"

    query = ''
    for i in message.command[1:]:
        query += ' ' + str(i)
    print(query)
    await lel.edit("🎵 **Processing**")
    ydl_opts = {"format": "bestaudio[ext=m4a]"}
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        url = f"https://youtube.com{results[0]['url_suffix']}"
        #print(results)
        title = results[0]["title"][:40]       
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f'thumb{title}.jpg'
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, 'wb').write(thumb.content)
        duration = results[0]["duration"]
        url_suffix = results[0]["url_suffix"]
        views = results[0]["views"]

    except Exception as e:
        await lel.edit("Song not found.Try another song or maybe spell it properly.")
        print(str(e))
        return

    keyboard = InlineKeyboardMarkup(
            [   
                [
                               
                    InlineKeyboardButton('📖 Playlist', url='t.me/SHIVAM9412'),
                    InlineKeyboardButton('Menu ⏯ ', url='t.me/SHIVAM9412')
                
                ],                     
                [
                    InlineKeyboardButton(
                        text="Watch On YouTube 🎬",
                        url=f"{url}")

                ],
                [       
                    InlineKeyboardButton(
                        text="❌ OWNERS",
                        url='https://t.me/SHIVAM9412')

                ]                             
            ]
        )
    requested_by = message.from_user.first_name
    await generate_cover(requested_by, title, views, duration, thumbnail)  
    file_path = await converter.convert(youtube.download(url))
  
    if message.chat.id in callsmusic.pytgcalls.active_calls:
        position = await queues.put(message.chat.id, file=file_path)
        qeue = que.get(message.chat.id)
        s_name = title
        r_by = message.from_user
        loc = file_path
        appendable = [s_name, r_by, loc]
        qeue.append(appendable)
        await message.reply_photo(
        photo="final.png", 
        caption=f"#⃣ Your requested song **queued** at position {position}!",
        reply_markup=keyboard)
        os.remove("final.png")
        return await lel.delete()
    else:
        chat_id = message.chat.id
        que[chat_id] = []
        qeue = que.get(message.chat.id)
        s_name = title            
        r_by = message.from_user
        loc = file_path
        appendable = [s_name, r_by, loc]      
        qeue.append(appendable)
        callsmusic.pytgcalls.join_group_call(message.chat.id, file_path)
        await message.reply_photo(
        photo="final.png",
        reply_markup=keyboard,
        caption="✯𝗩𝗖✯▶️ **Playing** here the song requested by {} 😜".format(
        message.from_user.mention()
        ),
    )
        os.remove("final.png")
        return await lel.delete()


@Client.on_message(
    filters.command("dplay")
    & filters.group
    & ~ filters.edited
)
async def deezer(client: Client, message_: Message):
    global que
    lel = await message_.reply("🔄 **Processing**")
    administrators = await get_administrators(message_.chat)
    chid = message_.chat.id
    try:
        user = await USER.get_me()
    except:
        user.first_name =  "VCPlayBot"
    usar = user
    wew = usar.id
    try:
        #chatdetails = await USER.get_chat(chid)
        lmoa = await client.get_chat_member(chid,wew)
    except:
           for administrator in administrators:
                      if administrator == message_.from_user.id:  
                          try:
                              invitelink = await client.export_chat_invite_link(chid)
                          except:
                              await lel.edit(
                                  "<b>Add me as admin of yor group first</b>",
                              )
                              return

                          try:
                              await USER.join_chat(invitelink)
                              await USER.send_message(message_.chat.id,"I joined this group for playing music in VC")
                              await lel.edit(
                                  "<b> userbot joined your chat</b>",
                              )

                          except UserAlreadyParticipant:
                              pass
                          except Exception as e:
                              #print(e)
                              await lel.edit(
                                  f"<b>🔴 Flood Wait Error 🔴 \nUser {user.first_name} couldn't join your group due to heavy requests for userbot! Make sure user is not banned in group."
                                  "\n\nOr manually add @patriciaXmusic to your Group and try again</b>",
                              )
                              pass
    try:
        chatdetails = await USER.get_chat(chid)
        #lmoa = await client.get_chat_member(chid,wew)
    except:
        await lel.edit(
            f"<i>Looks like  Userbot not in this chat, Ask admin to send /play command for first time or add assistant manually</i>"
        )
        return                            
    requested_by = message_.from_user.first_name   

    text = message_.text.split(" ", 1)
    queryy = text[1]
    res = lel
    await res.edit(f"Searching 👀👀👀 for `{queryy}` on deezer")
    try:
        arq = ARQ("https://thearq.tech")
        r = await arq.deezer(query=queryy, limit=1)
        title = r[0]["title"]
        duration = int(r[0]["duration"])
        thumbnail = r[0]["thumbnail"]
        artist = r[0]["artist"]
        url = r[0]["url"]
    except:
        await res.edit(
            "Found Literally Nothing, You Should Work On Your English!"
        )
        is_playing = False
        return
    keyboard = InlineKeyboardMarkup(
         [   
             [
                 InlineKeyboardButton('📖 Playlist', url='t.me/SHIVAM9412'),
                 InlineKeyboardButton('Menu ⏯ ', url='t.me/SHIVAM9412')     
             ],                     
             [
                 InlineKeyboardButton(
                     text="Listen On Deezer 🎬",
                     url=f"{url}")

             ],
             [       
                 InlineKeyboardButton(
                     text="❌ Close",
                     url='t.me/SHIVAM9412')

            ]                      
         ]
     )
    file_path= await converter.convert(wget.download(url))
    await res.edit("Generating Thumbnail")
    await generate_cover(requested_by, title, artist, duration, thumbnail)
    if message_.chat.id in callsmusic.pytgcalls.active_calls:
        await res.edit("adding in queue")
        position = await queues.put(message_.chat.id, file=file_path)       
        qeue = que.get(message_.chat.id)
        s_name = title
        r_by = message_.from_user
        loc = file_path
        appendable = [s_name, r_by, loc]
        qeue.append(appendable)
        await res.edit_text(f"✯𝗩𝗖✯=#️⃣ Queued at position {position}")
    else:
        await res.edit_text("✯𝗩𝗖✯=▶️ Playing.....")
        chat_id = message_.chat.id
        que[chat_id] = []
        qeue = que.get(message_.chat.id)
        s_name = title
        r_by = message_.from_user
        loc = file_path
        appendable = [s_name, r_by, loc]
        qeue.append(appendable)
        callsmusic.pytgcalls.join_group_call(message_.chat.id, file_path)

    await res.delete()

    m = await client.send_photo(
        chat_id=message_.chat.id,
        reply_markup=keyboard,
        photo="final.png",
        caption=f"Playing [{title}]({url}) Via Deezer"
    ) 
    os.remove("final.png")



@Client.on_message(
    filters.command("splay")
    & filters.group
    & ~ filters.edited
)
async def jiosaavn(client: Client, message_: Message):
    global que
    lel = await message_.reply("🔄 **Processing**")
    administrators = await get_administrators(message_.chat)
    chid = message_.chat.id
    try:
        user = await USER.get_me()
    except:
        user.first_name =  "VCPlayBot"
    usar = user
    wew = usar.id
    try:
        #chatdetails = await USER.get_chat(chid)
        lmoa = await client.get_chat_member(chid,wew)
    except:
           for administrator in administrators:
                      if administrator == message_.from_user.id:  
                          try:
                              invitelink = await client.export_chat_invite_link(chid)
                          except:
                              await lel.edit(
                                  "<b>Add me as admin of yor group first</b>",
                              )
                              return

                          try:
                              await USER.join_chat(invitelink)
                              await USER.send_message(message_.chat.id,"I joined this group for playing music in VC")
                              await lel.edit(
                                  "<b>helper userbot joined your chat</b>",
                              )

                          except UserAlreadyParticipant:
                              pass
                          except Exception as e:
                              #print(e)
                              await lel.edit(
                                  f"<b>🔴 Flood Wait Error 🔴 \nUser {user.first_name} couldn't join your group due to heavy requests for userbot! Make sure user is not banned in group."
                                  "\n\nOr manually add @patriciaXmusic to your Group and try again</b>",
                              )
                              pass
    try:
        chatdetails = await USER.get_chat(chid)
        #lmoa = await client.get_chat_member(chid,wew)
    except:
        await lel.edit(
            "<i>  helper Userbot not in this chat, Ask admin to send /play command for first time or add assistant manually</i>"
        )
        return     
    requested_by = message_.from_user.first_name
    chat_id=message_.chat.id
    text = message_.text.split(" ", 1)
    query = text[1]
    res = lel
    await res.edit(f"Searching 👀👀👀 for `{query}` on jio saavn")
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"https://jiosaavnapi.bhadoo.uk/result/?query={query}"
            ) as resp:
                r = json.loads(await resp.text())
        sname = r[0]["song"]
        slink = r[0]["media_url"]
        ssingers = r[0]["singers"]
        sthumb = r[0]["image"]
        sduration = int(r[0]["duration"])
    except Exception as e:
        await res.edit(
            "Found Literally Nothing!, You Should Work On Your English."
        )
        print(str(e))
        is_playing = False
        return
    keyboard = InlineKeyboardMarkup(
         [   
             [
               InlineKeyboardButton('📖 Playlist', url='t.me/SHIVAM9412'),
               InlineKeyboardButton('Menu ⏯ ', url='t.me/SHIVAM9412')
             ],                     
             [
               InlineKeyboardButton(
                   text="Join Updates Channel",
                   url='https://t.me/patricia_updates')
             ],
             [       
               InlineKeyboardButton(
                   text="❌ Close",
                   url='t.me/SHIVAM9412')

            ]                          
         ]
     )
    file_path= await converter.convert(wget.download(slink))
    if message_.chat.id in callsmusic.pytgcalls.active_calls:
        position = await queues.put(message_.chat.id, file=file_path)
        qeue = que.get(message_.chat.id)
        s_name = sname
        r_by = message_.from_user
        loc = file_path
        appendable = [s_name, r_by, loc]
        qeue.append(appendable)
        await res.delete()
        m = await client.send_photo(
            chat_id=message_.chat.id,
            reply_markup=keyboard,
            photo="final.png",
            caption=f"✯𝗩𝗖✯=#️⃣ Queued at position {position}",
        
        )           
           
    else:
        await res.edit_text("✯𝗩𝗖✯=▶️ Playing.....")
        chat_id = message_.chat.id
        que[chat_id] = []
        qeue = que.get(message_.chat.id)
        s_name = sname
        r_by = message_.from_user
        loc = file_path
        appendable = [s_name, r_by, loc]
        qeue.append(appendable)
        callsmusic.pytgcalls.join_group_call(message_.chat.id, file_path)
    await res.edit("Generating Thumbnail.")
    await generate_cover(requested_by, sname, ssingers, sduration, sthumb)
    await res.delete()
    m = await client.send_photo(
        chat_id=message_.chat.id,
        reply_markup=keyboard,
        photo="final.png",
        caption=f"Playing {sname} Via Jiosaavn",
        
    )
    os.remove("final.png")

# Have u read all. If read RESPECT :-)
