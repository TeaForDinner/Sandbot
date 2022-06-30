import discord
import os
from discord.ext import commands 
client = discord.Client()

client = commands.Bot(command_prefix = '$')


@client.event
async def blop(message):
    if message.author != client.user:
        await message.channel.send("blop")


@client.event
async def on_message(message):
    if message.content.startswith('blep'):
        await message.channel.send('blop')


@client.command()
async def blep(ctx):
  await ctx.send('Blup')
  


my_secret = os.environ['bot_secret']
client.run(my_secret)
#DO NOT PUT THE CODE AFTER HERE
