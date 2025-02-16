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

# PURGE

async def purge(amount: int, message):
    if amount > 50:
        await message.channel.send("Purge limit is 50. Deleting 50 messages...")
        amount = 49
    await message.channel.purge(limit=amount)
    return

# KICK

async def kick(message: Message, user_id, reason):
    if user_id[:2] == "<@" and user_id[-1] == ">": user_id = user_id[2:-1]

    user = await message.guild.fetch_member(user_id)
    globalname = user.name

    try: await message.guild.kick(user, reason=reason)

    except Forbidden: await message.channel.send("You don't have permission to kick this member.")
    except HTTPException: await message.channel.send("Kicking failed. Possibly server error.")
    except NotFound: await message.channel.send("User does not exist in the server.")

    else:
        if not reason: await message.channel.send(f"Successfully kicked {globalname}.")
        else: await message.channel.send(f"Successfully kicked {globalname} with the reason: \"{reason}\"")

# BAN

async def ban(message: Message, self: Client, user_id, reason):
    if user_id[:2] == "<@" and user_id[-1] == ">": user_id = user_id[2:-1]

    user = await self.fetch_user(user_id)
    globalname = user.name

    try: await message.guild.ban(user, reason=reason)

    except Forbidden: message.channel.send("You don't have the permission to kick this member.")
    except HTTPException: message.channel.send("Ban failed. Possibly server error.")
    except NotFound: message.channel.send("User does not exist in the server.")

    else: 
        if not reason: await message.channel.send(f"Successfully banned {globalname}") 
        else: await message.channel.send(f"Successfully banned {globalname} with the reason \"{reason}\"")

# UNBAN

async def unban(message: Message, self: Client, user_id):
    user = await self.fetch_user(user_id)
    globalname = user.name

    try: await message.guild.unban(user)

    except NotFound: message.channel.send("User is either non-existent or not banned.")
    except Forbidden: message.channel.send("You don't have the permission to unban this user.")
    except HTTPException: message.channel.send("Unban failed. Possibly server error.")

    else: await message.channel.send(f"Successfully unbanned {globalname}.")