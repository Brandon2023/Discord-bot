import discord 
import time
from discord.ext import commands

token = 'OTQ1ODQwMjM0MDQ0NzM5NTk1.YhWAXA.wDIXnMluro1tY71sNK8vmQHOWzU'
client = discord.Client()

client = commands.Bot(command_prefix='$')

@client.event
async def on_ready():
    print("Bot has connected to discord")

@client.command()
async def test(ctx):
    await ctx.send("its working lol")

@client.command()
async def help(ctx):
    await ctx.send("")

@client.command()
async def thefunny(ctx):
    while True: 
        time.sleep(2)
        await ctx.send("@everyone")   









client.run(token)
