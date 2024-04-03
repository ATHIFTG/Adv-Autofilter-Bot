# 💝
from pyrogram import Client, filters
import requests
from info import *
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from urllib.parse import quote
import json




@Client.on_message(filters.command('gpt4'))
async def chat_gpt(client, message):   
    text = "".join(message.text.split(" ")[1:])
    user_input = message.text.split()[1:]
    if not user_input:
       await message.reply_text("Give An Input !!")
    if len(text) == 0:return await message.reply_text(
            "Give An Inlut !!", parse_mode=ParseMode.MARKDOWN 
        )
    msg = await message.reply_text("⏳")
    url = "https://api.safone.dev/chatgpt"
    payloads = {
          "message": text,
          "version": 4,
          "chat_mode": "assistant",
          "dialog_messages": "[{\"bot\":\"\",\"user\":\"\"}]"
          }
    headers = {"Content-Type" : "application/json"}
    try:
         response = requests.post(url, json=payloads, headers=headers)
         results = response.json()
         res = results["message"]    
         await message.reply_text(f"ʜᴇʏ: {message.from_user.mention}\n\nϙᴜᴇʀʏ: {user_input}\n\nʀᴇsᴜʟᴛ:\n\n{res}")
         reply_markup = InlineKeyboardMarkup(buttons)
    except Exception as e:
         await message.reply_text(f"**Error {e}" )
