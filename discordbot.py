import discord 

token = 'INSERT DISCORD BOT TOKEN HERE'
client = discord.Client()

@client.event
async def on_ready():
    print("Bot has connected to discord!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('~test'):
        await message.channel.send('Hi')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('~test2'):
        await message.channel.send('hello test2')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('~test3'):
        await message.channel.send('hello test3')

client.run(token)
