from discord.ext import commands
import discord
import asyncio
import os 

	
class SoundboardCog(commands.Cog):
	def __init__(self, bot, folder):
		self.bot = bot 
		self.folder = folder
		self.sound_list = SoundboardCog.loadAudio(self.folder)


	@staticmethod
	def loadAudio(folder):
		FileList = os.listdir(folder)
		if not FileList:
			raise Exception("The audio folder is empty")
		sound_list = []
		for file in FileList:
			if ".mp3" in file:
				sound_list.append(file.replace(".mp3",""))
		print(sound_list)			
		return sound_list


	@commands.command(name='join',description="This commanded needs to be run first before all other commands") 
	async def join(self,ctx):
		author = ctx.message.author
		if author.voice != None:
			print("joined")
			VoiceChannel = author.voice.channel
			vc = await VoiceChannel.connect()
			if 'Welcome' in self.sound_list:
				vc.play(discord.FFmpegPCMAudio(self.folder + '/'+ 'Welcome' + '.mp3'), after=lambda e: print('done', e))
		return 

	@commands.command(name="kick",description="kicks bot outta channel")
	async def LeaveChannel(self,ctx):
		for x in self.bot.voice_clients:
			if(x.guild == ctx.message.guild):
				x.play(discord.FFmpegPCMAudio(self.folder + '/'+ 'Bye' + '.mp3'), after=lambda e: print('done', e))
				await asyncio.sleep(14)
				return await x.disconnect()

	
	@commands.command(name="play", description = "Requires u and bot to be in a voice channel first ie !join command")
	async def play_audio(self,ctx,*,message):
		print(self.bot.voice_clients)
		author = ctx.message.author
		if not self.bot.voice_clients:
				response = author.mention + " BOT MUST BE IN VOICE CHANNEL DUMASS"
				await ctx.send(response) 
				print("Requires you to be in voice channel")
		elif author.voice == None:
			await ctx.send(author.mention + " PLS READ INSTRUCTIONS. NEED TO BE IN BOTS VOICE CHANNEL DUMASS")
		else: 
			for x in self.bot.voice_clients:
				if(x.guild == ctx.message.guild):
					if message in self.sound_list and author.voice.channel == x.channel:
						x.play(discord.FFmpegPCMAudio(self.folder + '/'+ message + '.mp3'), after=lambda e: print('done', e))
	
						
				


	@commands.command(name = "playCommands", description = "displays all commands for the sounds")
	async def getCommands(self,ctx):
		counter =1
		msg=ctx.author.mention +'\n'
		for file in self.sound_list:
			msg = msg + str(counter) +'.' + " !play " + file+'\n'
			counter+=1
		await ctx.message.channel.send(msg)

	



