import time
import discord
import asyncio

client = discord.Client() #nom du bot

@client.event
async def on_ready(): #quand le bot est logged in
      print("Logged in as :", client.user.name)
      print("ID :", client.user.id)

@client.event
async def on_message(message): #quand le bot lit un message
      if message.author == client.user:
            return

      elif message.content == "$ping":
            await client.send_message(message.channel, ":ping_pong: **Pong !**")
            
      elif message.content == "Bonjour":
            await client.send_message(message.channel, "**>HELLO WORLD !!! **")

client.run("NDIyMDgyNjUwNjY1Mzg1OTkz.DZPgaQ.BO-2dFAjU6YFezVDGWGcBeE5Xo8")
      
      
