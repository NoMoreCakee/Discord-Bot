import dotenv, asyncio
from discord import *
from discord.ext import commands

dotenv.load_dotenv()

prefix = '$'

# class DCClient(Client):

#     async def on_message(self, message):
#         if not message.content[0] == prefix:
#             return
        
#         command = message.content[1::].split(' ')[0]
#         args = message.content[1::].split(' ')[1:]

#         print(f"Command from {message.author}: {command}")
#         print(f'Arguments: {args}')
            
        
#         if command == 'help':
#             await message.channel.send(send_help())
            

#         if command == "purge":
#             if len(args) < 1:
#                 await message.channel.send("Please provide the amount of messages to purge.")
#                 return
            
#             if not args[0].isdigit():
#                 await message.channel.send("Please only provide digits.")

#             await purge(int(args[0]), message)

#         if command == "kick":
#             reason = None
#             if len(args) >= 2:
#                 reason = " ".join(args[1::])
#                 print(reason)
#             await kick(message, args[0], reason)

#         if command == "ban":
#             reason = None
#             if len(args) >= 2:
#                 reason = " ".join(args[1::])
#                 print(reason)
#             await ban(message, self, args[0], reason)

#         if command == "unban":
#             await unban(message, self, args[0])



intents = Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=prefix, intents=intents)

async def load_cogs():
    await bot.load_extension("cogs.moderation")

@bot.event
async def on_ready():
        print(f"Logged on as {bot.user}!")

# @bot.command()
# async def rolldice(ctx, arg):
#     if len(arg) > 0:
#         for i in arg:
#             if not i.isdigit():
#                 await ctx.send("Please only provide digits.")
#                 return
#             if int(i) <= 0:
#                 await ctx.send("Values can't be negative.")
#                 return
#     if not arg:
#         ret_value = await roll(message=message)
#         if ret_value:
#             await ctx.send(ret_value)
#     if len(arg) == 1:
#         ret_value = await roll(int(arg[0]), message=message)
#         if ret_value:
#             await ctx.send(ret_value)
#     if len(arg) > 1:
#         ret_value = await roll(int(arg[0]), int(arg[1]), message=message)
#         if ret_value:
#             await ctx.send(ret_value)

async def main():
    await load_cogs()
    await bot.start(dotenv.get_key(".env","API_KEY"))

asyncio.run(main())