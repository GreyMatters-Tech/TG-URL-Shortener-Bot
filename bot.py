import asyncio
import datetime
import logging
import logging.config
import sys
from pyrogram import *
from pyrogram.errors.exceptions.not_acceptable_406 import *
from config import *
from database import *
from database.users import *
from aiohttps import *
from helpers import *
from pyshortner import *
logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.INFO)
import os
import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)



if __name__ == "__main__" :

    plugins = dict(
        root="plugins"
    )
    GreyMattersTech = Client(
        "Mdisk-Pro",
        bot_token=BOT_TOKEN,
        api_id=API_ID,
        api_hash=API_HASH,
        plugins=plugins
    )
    
    async def start(self):
        me = await self.get_me()
        self.owner = await self.get_users(int(OWNER_ID))
        self.username = f'@{me.username}'
        temp.BOT_USERNAME = me.username
        temp.FIRST_NAME = me.first_name
        if not await db.get_bot_stats():
            await db.create_stats()
        banned_users = await filter_users({"banned": True})
        async for user in banned_users:
            temp.BANNED_USERS.append(user["user_id"])
        logging.info(LOG_STR)
        await broadcast_admins(self, '** Bot started successfully **\n\nBot By @GreyMattersTech')
        logging.info('Bot started')


    GreyMattersTech.run()

# Removed Upper All Codes Because This is Not Required Now. 

#SESSION = "GreyMattersTech"

#class Bot(Client):

    #def __init__(self):
        #super().__init__(
           # name=SESSION,
            #api_id=API_ID,
           # api_hash=API_HASH,
           # bot_token=BOT_TOKEN,
            #workers=50,
           # plugins={"root": "plugins"},
            #sleep_threshold=5,
        #)



    async def stop(self, *args):
        await super().stop()
        logging.info("Bot stopped. Bye.")

#GreyMattersTech = Bot()
#GreyMattersTech.run()
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
