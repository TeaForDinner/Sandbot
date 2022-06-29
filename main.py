import discord
import os

client = discord.Client()


@client.event
async def blop(message):
  if message.author != client.user and message.content.lower() == "blep":
    blop = "blop"
    await message.channel.send(blop)


my_secret = os.environ['bot_secret']
client.run(my_secret)