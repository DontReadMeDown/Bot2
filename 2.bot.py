import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('sa'):
        await message.channel.send(f' as hoş geldin')
    
    if message.content.startswith('merhaba'):
        await message.channel.send(f' merhabalar!')
    if message.content.startswith('bot'):
        await message.channel.send(f' efendim?')
    
    if message.content.startwhit('havalı bot')
    await message.channel.send(f'https://cdn.discordapp.com/attachments/1191831120447291515/1269739701246365797/image.png?ex=66b128bf&is=66afd73f&hm=ae63b5f717dc1a7d174d51ee370102e8f608a5c0b44889f513b305046333bf83&')
        
client.run("")