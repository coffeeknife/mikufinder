#!/usr/bin/env python3

import os, discord

TOKEN = os.getenv("BOT_TOKEN")

if TOKEN == None:
    exit(1)

class MikuFinder(discord.Client):
    async def on_ready(self):
        pass

intents = discord.Intents.default()
#intents.message_content = True

client = MikuFinder(intents=intents)
client.run(TOKEN)