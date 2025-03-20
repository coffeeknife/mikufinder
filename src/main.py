#!/usr/bin/env python3

from loguru import logger
import os, discord

TOKEN = os.getenv("BOT_TOKEN")

if TOKEN == None:
    logger.critical("Please set BOT_TOKEN to your bot token in the environment.")
    exit(1)

class MikuFinder(discord.Client):
    async def on_ready(self):
        logger.success(f'Logged in as {self.user}!')

intents = discord.Intents.default()
intents.message_content = True

client = MikuFinder(intents=intents)
client.run('token')