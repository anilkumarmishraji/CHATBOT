import asyncio
from os import getenv
from config import OWNER_ID
from dotenv import load_dotenv
from pyrogram import Client
from pytgcalls import PyTgCalls
from pytgcalls.types import Update
import config


class Userbot(Client):
    def __init__(self):
        self.one = Client(
            name="VIPAss1",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING1),
            no_updates=False,
            plugins=dict(root="nexichat.idchatbot"),
        )
        
        self.calls = PyTgCalls(self.one)

    async def start(self):
        print(f"Starting Id chatbot...")

        if config.STRING1:
            await self.one.start()
            try:
                await self.one.join_chat("THE_VIP_BOY")
                await self.one.join_chat("THE_VIP_BOY_OP")
                await self.one.join_chat("TG_FRIENDSS")
                await self.one.join_chat("VIP_CREATORS")
            except:
                pass
            self.one.id = self.one.me.id
            self.one.name = self.one.me.mention
            self.one.username = self.one.me.username

            
            await self.calls.start()

            print(f"Id-Chatbot Started as {self.one.me.first_name}")
            
            
            @self.calls.on_update()
            async def on_call_update(update: Update):
                print(f"Voice chat update received: {update}")
        
    async def stop(self):
        print(f"Stopping Id-Chatbot...")
        try:
            if config.STRING1:
                await self.calls.stop() 
                await self.one.stop()
        except:
            pass
