import discord 
client = discord.client()
token = ''

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
        await message.channel.send('Here is a list of commands: ')


client.run(token)