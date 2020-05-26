# bot.py
import os
import sys
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
l5v5 = []
lparty = []
lsoloduo = []
client = discord.Client()
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$queue'):
        parser = message.content.split()
        if parser[1] == "customs" or parser[1] == "5s":
            if message.author in l5v5:
                await message.channel.send("You're already in that queue. :/")
                return
        
            l5v5.append(message.author)
            if len(l5v5) == 10:
                await message.channel.send("Now starting custom channels")
                #Move players into channels
            await message.channel.send(parser[1] + " is looking for " + str(10 - len(l5v5)) + " more people for customs!")
            
        elif parser[1] == "party" or parser[1] == "normals" or parser[1] == "league":
            if message.author in lparty:
                await message.channel.send("You're already in that queue. :/")
                return
            lparty.append(message.author)
            if len(lparty) > 1: # Todo or if there is someone already in the channel
                await message.channel.send(lparty[0] + " and" + lparty[1] + " sitting in a tree")
                
client.run(TOKEN)

