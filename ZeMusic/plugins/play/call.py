import asyncio
from pyrogram import Client, filters
from strings.filters import command
from pyrogram.types import Message, ChatPrivileges
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic.core.call import Mody
from ZeMusic.utils.database import get_assistant

@app.on_message(filters.video_chat_started)
async def stcall(client: Client, message: Message): 
      Startt = "الكول اتفتح 🙈♥"
      await message.reply_text(Startt)

@app.on_message(filters.video_chat_ended)
async def encall(client: Client, message: Message): 
      Enddd = "قفلت الكول ليه ربنا يسمحك 😔😭"
      await message.reply_text(Enddd)

@app.on_message(filters.voice_chat_members_invited)
async def zoharyy(client: Client, message: Message): 
           text = f"-قام {message.from_user.mention}\n - بدعوتك للكول ي رايق 🥺♥ : "
           x = 0
           for user in message.video_chat_members_invited.users:
             try:
               text += f"[{user.first_name}](tg://user?id={user.id}) "
               x += 1
             except Exception:
               pass
           try:
             await message.reply(f"{text} ")
           except:
             pass
