import random
from discord import *

# ROLL

async def roll(count=1, sides=6, message=None):
    rolls = []
    poss_sides = [2, 3, 4, 5, 6, 8, 10, 12, 16, 20, 50, 100]
    message_out = ""

    if count > 10:
        await message.channel.send("Count limit is 10.")
        return
    
    if sides not in poss_sides:
        out_message = "> Please only use these values as sides: "
        for s in poss_sides:
            if s != poss_sides[-1]:
                out_message += f"{s}, "
            else: out_message += f"{s}."
        return out_message

    for _ in range(0, count):
        rolls.append(random.randint(1, sides))

    for c in range(0, len(rolls)):
        message_out += f"> Roll {c+1}: `{rolls[c]}`\n"

    if len(rolls) > 1: message_out += f"> \n > :game_die: Sum: {sum(rolls)}"

    return message_out


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

# PURGE

async def purge(amount: int, message):
    if amount > 50:
        await message.channel.send("Purge limit is 50. Deleting 50 messages...")
        amount = 49
    await message.channel.purge(limit=amount)
    return
