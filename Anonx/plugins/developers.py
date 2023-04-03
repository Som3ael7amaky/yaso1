import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonX import app
from random import  choice, randint

#       #             #  #####  #####      ####
#        #           #  #         #            #     #
#          #        #  #####   #            #####     
#           #    #    #          #     ##    #     #
#              #       #####   ######   #     #
                
                
@app.on_message(
    command(["مطورين سي ار","مساعد المطورين","مطورين","مطورين ✘"])
    & ~filters.edited
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/61a35e2f797aa6723764b.jpg",
        caption=f"""**⩹━★⊷━⌞ ✘ • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝━⊶★━⩺**\nمرحبا بك عزيزي {message.from_user.mention} في قسم مطورين ✘ ميوزك\nللتحدث مع مطورين اضغط علي الازرار بالاسفل👇\n**⩹━★⊷━⌞ ✘ • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝━⊶★━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒ꐞꈼꌚꂦꂦ⌯►", url=f"https://t.me/U_U_Q_1"), 
                 ],[
                    InlineKeyboardButton(
                        "ֆ0ʍɛǟ", url=f"https://t.me/C_C_Q_1"),
                ],[
                    InlineKeyboardButton(
                        "doma", url=f"https://t.me/U_U_C_1"),
                ],[
                
                    InlineKeyboardButton(
                        "★⌞ ✘ • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝⚡", url=f"https://t.me/C_U_U_1"),
                ],

            ]

        ),

    )








@app.on_message(
    command(["دووما انجم","ادهم","دومي","مبرمج","doma","doma" ,"مساعد المطور"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("U_U_C_1")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━★⊷━⌞ ✘ • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝━⊶★━⩺\n\n🧞‍♂️ ¦𝙽𝙰𝙼𝙴 :{name}\n🎯 ¦𝚄𝚂𝙴𝚁 :@{usr.username}\n💣 ¦𝙸𝙳 :`{usr.id}`\n🚀 ¦𝙱𝙸𝙾 :{usr.bio}\n\n**⩹━★⊷━⌞ ✘ • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝━⊶★━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )


@app.on_message(
    command(["يســو يـنق۾","يسـوو","اسماعيل","ٱلمشمبرمج","yasoo","سمعه"]])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("C_C_Q_1")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━★⊷━⌞ ✘ • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝━⊶★━⩺\n\n🧞‍♂️ ¦𝙽𝙰𝙼𝙴 :{name}\n🎯 ¦𝚄𝚂𝙴𝚁 :@{usr.username}\n💣 ¦𝙸𝙳 :`{usr.id}`\n🚀 ¦𝙱𝙸𝙾 :{usr.bio}\n\n**⩹━★⊷━⌞ ✘ • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝━⊶★━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )


@app.on_message(
    command("يســو يـنق۾","يسـوو","اسماعيل","ٱلمشمبرمج","yasoo","سمعه")
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("U_U_Q_1")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━★⊷━⌞ ✘ • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝━⊶★━⩺\n\n🧞‍♂️ ¦𝙽𝙰𝙼𝙴 :{name}\n🎯 ¦𝚄𝚂𝙴𝚁 :@{usr.username}\n💣 ¦𝙸𝙳 :`{usr.id}`\n🚀 ¦𝙱𝙸𝙾 :{usr.bio}\n\n**⩹━★⊷━⌞ ✘ • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝━⊶★━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )
    


@app.on_message(
    command(["/api"])
    & ~filters.edited
    
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/61a35e2f797aa6723764b.jpg",
        caption=f"""**⩹⊷━⌞ ✘ • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝━━⩺**\nمرحبا بك عزيزي {message.from_user.mention} في قسم الذكاء الاصتناعي الخاص بسورس ✘\nلتتمكن من استخدام اوامر الذكاء الاصتناعي اكتب \n /gpt + السؤال بالاسفل👇\n**⩹━━⌞ ✘ • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝━━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒ꐞꈼꌚꂦꂦ⌯‹", url=f"https://t.me/U_U_Q_1"), 
                 ],[
                
                    InlineKeyboardButton(
                        "★⌞ ✘ • 𝙎𝙊𝙐𝙍𝘾𝙀 ⌝⚡", url=f"https://t.me/C_U_U_1"),
                ],

            ]

        ),

    )



    