import discord 
import time
from discord.ext import commands

token = ''
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
async def idk(ctx):
   









client.run(token)
