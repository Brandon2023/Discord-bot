import discord 
from discord.ext import commands

token = ''
client = discord.Client()

client = commands.Bot(command_prefix='$')

@client.event
async def on_ready():
    print("Bot has connected to discord")

@client.command()
async def test1(ctx):
    await ctx.send("test1 is successful")


client.run(token)
