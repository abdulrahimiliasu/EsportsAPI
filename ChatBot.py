import os
import random
import discord

from discord.ext import commands

#from dotenv import load_dotenv uncomment if you want to use .env
'''
load_dotenv()
TOKEN = os.getenv('name of .env token')
'''
client = discord.Client()
bot = commands.Bot(command_prefix='%%')

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    responses = ['Welcome Governor','Hello Hello','You Are Awesome']

    if message.content == 'Hello':
        response = random.choice(responses)
        await message.channel.send(response)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if 'happy birthday' in message.content.lower():
        await message.channel.send('Happy Birthday! 🎈🎉')

@bot.command(name='Start')
async def nine_nine(ctx):

    response = 'I am a Robot'
    await ctx.send(response)

client.run('Nzg2NDE3NDg5NzI1ODgyMzg4.X9GGXA.xS7Lb6mZ-ioUAffBIZ7r5suG_BI')
# bot.run('Nzg2NDE3NDg5NzI1ODgyMzg4.X9GGXA.xS7Lb6mZ-ioUAffBIZ7r5suG_BI') uncomment to run bot command
