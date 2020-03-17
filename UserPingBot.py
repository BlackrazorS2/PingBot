import discord
from discord.ext import commands
import asyncio
import random

TOKEN = TOKEN
USER_ID = USER_ID
SERVER_ID = SERVER_ID


client = commands.Bot(command_prefix='!') # command is !
client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='!hpd <number>'))
    print('ready boss!')

@client.command()
async def hpd(ctx, num):
    try:
        if int(num) <= 10:
            for i in range(1, int(num)+1):
                await ctx.send(f"hpd <@{USER_ID}>")
        else:
            await ctx.send("Excessive amount of pings!")
    except:
        await ctx.send("Something broke! Did you enter a valid number?")

async def passive_ping():
    try:
        await client.wait_until_ready() 
        time = random.randint(900,1801)
        server = client.get_guild(SERVER_ID)
        channels = server.channels
        channel_num =  random.randint(0, len(channels))
        await channels[channel_num].send(f"hpd <@{USER_ID}>")
        await asyncio.sleep(time) # waits 30 min
    except:
        pass
client.loop.create_task(passive_ping())
client.run(TOKEN)