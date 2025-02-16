import os
import dotenv
import asyncio
import discord
from discord.ext import commands

dotenv.load_dotenv()

prefix = '$'
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=prefix, intents=intents)


async def load_cogs():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")


@bot.event
async def on_ready():
    print(f"Logged on as {bot.user}!")


async def main():   
    async with bot:
        await load_cogs()
        await bot.start(dotenv.get_key(".env","API_KEY"))

asyncio.run(main())