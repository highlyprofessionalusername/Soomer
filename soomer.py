import discord
import logging
# logging.basicConfig(Level=logging.WARNING)

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    for i in range(len(client.guilds)):
        print(client.guilds[i])

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('42069'):
        await message.channel.send('Yeet')
        print(message.guild)



# class MyClient(discord.Client):
#     async def on_ready(self):
#         print('Logged on as {0}!'.format(self.user))

#     async def on_message(self, message):
#         print('Message from {0.author}: {0.content}'.format(message))

client.run('$YOURTOKENHERE')