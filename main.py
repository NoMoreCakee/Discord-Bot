import dotenv
from discord import *
from commands import *

dotenv.load_dotenv()

prefix = '$'

def send_help():
    return "> $roll <count> <sides>\n > Default value: 1d6"

class DCClient(Client):
    async def on_ready(self):
        print(f"Logged on as {self.user}!")

    async def on_message(self, message):
        if not message.content[0] == prefix:
            return
        
        command = message.content[1::].split(' ')[0]
        args = message.content[1::].split(' ')[1:]

        print(f"Command from {message.author}: {command}")
        print(f'Arguments: {args}')


        if command == 'roll':
            if len(args) > 0:
                for i in args:
                    if not i.isdigit():
                        await message.channel.send("Please only provide digits.")
                        return
                    if int(i) <= 0:
                        await message.channel.send("Values can't be negative.")
                        return
            if not args:
                ret_value = await roll(message=message)
                if ret_value:
                    await message.channel.send(ret_value)
            if len(args) == 1:
                ret_value = await roll(int(args[0]), message=message)
                if ret_value:
                    await message.channel.send(ret_value)
            if len(args) > 1:
                ret_value = await roll(int(args[0]), int(args[1]), message=message)
                if ret_value:
                    await message.channel.send(ret_value)
        
        if command == 'help':
            await message.channel.send(send_help())
            

        if command == "purge":
            if len(args) < 1:
                await message.channel.send("Please provide the amount of messages to purge.")
                return
            
            if not args[0].isdigit():
                await message.channel.send("Please only provide digits.")

            await purge(int(args[0]), message)

        if command == "kick":
            reason = None
            if len(args) >= 2:
                reason = " ".join(args[1::])
                print(reason)
            await kick(message, args[0], reason)

        if command == "ban":
            reason = None
            if len(args) >= 2:
                reason = " ".join(args[1::])
                print(reason)
            await ban(message, self, args[0], reason)

        if command == "unban":
            await unban(message, self, args[0])



intents = Intents.default()
intents.message_content = True

client = DCClient(intents=intents)
client.run(dotenv.get_key(".env","API_KEY"))