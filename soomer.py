"""
A Terrible Discord bot
"""
import sqlite3
import discord

conn = sqlite3.connect('emojilytics.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS emojidata (emoji text, message_used integer, reacc_used integer)''')
conn.commit()


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
    print("this message sent from "+ str(message.guild))
    print(message)
    print(message.channel.id)
    if message.channel.id == 773676386228502588: #/dev/null channel ID on cyberdelia
        await message.delete()



client.run('token')
