import asyncio, traceback
from config import OWNER_ID
from pyrogram import filters, Client as app
from pyrogram.errors.exceptions.bad_request_400 import UserIsBlocked

@app.on_message(filters.command("contact"))
async def contactAdmin(bot, message):
    try:
        user = "@" + message.from_user.username if message.from_user.username else message.from_user.mention
        if not message.reply_to_message:
            return await message.reply("Please use the method described in the image to contact admin[.](https://telegra.ph/file/9a4039a2d602486cf1c00.jpg)")
        if not message.reply_to_message.text:
            return await message.reply("Please use the method described in the image to contact admin[.](https://telegra.ph/file/9a4039a2d602486cf1c00.jpg)")
        await bot.send_message(
            chat_id=OWNER_ID, 
            text=f"<bold>From:</bold> {user} <bold>Id:</bold> <code>{message.chat.id}</code>\n{message.reply_to_message.text.html}"
        )
        userMsg = await bot.send_message(
            chat_id=message.chat.id,
            text="Your message has been successfully sent to Admin.",
            reply_to_message_id=message.reply_to_message.id
        )
        await asyncio.sleep(5)
        await userMsg.delete()
    except Exception as e:
        return await message.reply(f"**Traceback Info:**\n`{traceback.format_exc()}`\n**Error Text:**\n`{e}`")

@app.on_message(filters.private & filters.user(OWNER_ID))
async def replyUser(bot, message):
    try:
        if message.reply_to_message:
            chat = int(message.reply_to_message.text.split("\n")[0][-10::])
            try:
                await bot.send_message(
                    chat_id=chat,
                    text=message.text
                )
                adminMsg = await message.reply(
                    text="Successfully sent reply to User.",
                    quote=True
                )
                await asyncio.sleep(5)
                await adminMsg.delete()
            except UserIsBlocked:
                return await message.reply(
                    text="User has blocked me."
                )
    except Exception as e:
        return await message.reply(
            text=f"**Traceback Info:**\n`{traceback.format_exc()}`\n**Error Text:**\n`{e}`"
        )
"""
   _____                    __  __         _    _              _       _______           _     
  / ____|                  |  \/  |       | |  | |            ( )     |__   __|         | |    
 | |  __  _ __  ___  _   _ | \  / |  __ _ | |_ | |_  ___  _ __|/ ___     | |  ___   ___ | |__  
 | | |_ || '__|/ _ \| | | || |\/| | / _` || __|| __|/ _ \| '__| / __|    | | / _ \ / __|| '_ \ 
 | |__| || |  |  __/| |_| || |  | || (_| || |_ | |_|  __/| |    \__ \    | ||  __/| (__ | | | |
  \_____||_|   \___| \__, ||_|  |_| \__,_| \__| \__|\___||_|    |___/    |_| \___| \___||_| |_|
                      __/ |                                                                    
                     |___/                                                                     
Author: GreyMatter's Tech
GitHub: https://GreyMattersTech.com/GitHub
Website: https://GreyMattersTech.com
"""
