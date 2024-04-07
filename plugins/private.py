import logging
from config import *
import asyncio
from database.users import *
from pyrogram import *
from pyrogram.types import *
from bot import *
from pyrogram.errors.exceptions.bad_request_400 import *
import shortener
from shortener import *
from pyshortner import *
logger = logging.getLogger(__name__)

channel = UPDATE_CHANNEL

ft = f"Due To Overload Only Channel Subscribers can Use the Bot Join - @GreyMattersTech"


# Private Chat
@Client.on_message(filters.private)
async def private_link_handler(c: Client, message: Message):

    try:
        Fsub = await force_subs(c, message, channel, ft)
        if Fsub == True:
            return
        user = await get_user(message.from_user.id)
        ban = user["banned"]
        if ban is not False:
            await message.reply_text(f'You Are Banned')
            return 
        user = await get_user(message.from_user.id)
        if message.text and message.text.startswith('/'):
            return
        if message.text:
            caption = message.text.html
        elif message.caption:
            caption = message.caption.html
        if len(await extract_link(caption)) <= 0 and not message.reply_markup:
            return
        user_method = user["method"]
        vld = await user_api_check(user)
        if vld is not True:
            return await message.reply_text(vld)
        try:
            txt = await message.reply('`Converting.......`', quote=True)

            await mains_convertor_handlers(message, user_method, user=user)
            await update_stats(message, user_method)
            bin_caption = f"""{caption}

#NewPost
From User :- {message.from_user.mention} [`{message.from_user.id}`]"""

            try:
                if LOG_CHANNEL and message.media:
                    await message.copy(LOG_CHANNEL, bin_caption)
                elif message.text and LOG_CHANNEL:
                    await c.send_message(LOG_CHANNEL, bin_caption, disable_web_page_preview=True)
            except PeerIdInvalid as e:
                logging.error("Make sure that the bot is admin in your log channel")
        except Exception as e:
            logger.exception(e)
        finally:
            await txt.delete()
            
    except Exception as e:
        logging.exception(e, exc_info=True)
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
