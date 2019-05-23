from discord.ext.commands import Bot 
from Cogs.soundboard import SoundboardCog
import asyncio
import discord
import json 

with open ('config.json','r') as f:
	config = json.load(f)

TOKEN=config['token']
BOT_PREFIX = config['prefix']
client = Bot(command_prefix=BOT_PREFIX)
audioFolder = 'audio'


@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print('------')

@client.event
async def on_member_join(member):
	welcomeMessage = 'Welcome to ' + member.guild + "Channel"
	await member.send(welcomeMessage)

def main():
	client.add_cog(SoundboardCog(client,audioFolder))
	client.run(TOKEN)


if __name__ == '__main__':
	main()


