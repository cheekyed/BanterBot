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
welcomeMessage = 'Welcome to the channel'

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print('------')

@client.event
async def on_member_join(member):
	await member.send(welcomeMessage)

@client.command(name="set-welcome",description= "sets welcome message to new members for the server")
async def on_message(ctx,*,message):
	welcomeMessage = message 
	channel = ctx.message.channel
	await channel.send(ctx.message.author.mention+ " U Have Successfully Changed The Welcome Message To " + "\""+ welcomeMessage + "\"")

def main():
	client.add_cog(SoundboardCog(client,audioFolder))
	client.run(TOKEN)


if __name__ == '__main__':
	main()


