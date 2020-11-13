import discord
import logging
import re
import sqlite3

conn = sqlite3.connect('emojilytics.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS emojidata (emoji text, message_used integer, reacc_used integer)''')
conn.commit()

# logging.basicConfig(Level=logging.WARNING)

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    for i in range(len(client.guilds)):
        print("logged into server " + str(client.guilds[i]))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('42069'):
        print("this message sent from "+ str(message.guild))
        print()

client.run('$YOURTOKENHERE')