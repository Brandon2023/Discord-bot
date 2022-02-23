import discord 
client = discord.Client()
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

    elif message.content.startswith('~test2'):
        await message.channel.send('test2: ')
    
    elif message.content.startswith('~test3'):
        await message.channel.send('test3: ')


client.run(token)
