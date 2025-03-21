#!/usr/bin/env python3

import os, discord, logging, validators, requests, functions

logging.basicConfig(level=logging.INFO)

TOKEN = os.getenv("BOT_TOKEN")
logger = logging.getLogger('discord.mikufinder')

songlink = "https://api.song.link/v1-alpha.1/links"

if TOKEN == None:
    exit(1)

bot = discord.Bot()

@bot.event
async def on_ready():
    logger.info(f'Logged in as {bot.user}!')

@bot.command(description="test command")
async def ping(ctx):
    await ctx.respond("Pong!")

@bot.command(description="lookup music by link")
async def lookup(ctx, link: discord.Option(str, "music link", max_length=6000)):
    if validators.url(link):
        response = functions.lookupLink(link)
        await ctx.respond(embed = functions.buildEmbed(response))
    else:
        await ctx.respond(f'`{link}` is not a valid URL!', ephemeral=True)

bot.run(TOKEN)