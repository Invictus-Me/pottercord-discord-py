import discord
from discord.ext import commands
import random
import matplotlib
import pandas as pd
import numpy as np
from MemFunctions import getNishList, getSkwiList, checkSummer, getNimArts, YimYimIndexes
from MemFunctions import MembersList, getMembers, amandify, hayafying

import typing 

finalNishList = getNishList()
finalSkwiList = getSkwiList()

colorEmbed  = list(matplotlib.colors.cnames.values())
colorEmbed = [int(('0x'+ x[1:]), 16) for x in colorEmbed]
title = "POwOttercOwOrd"
description = "A Pottercord bot with a lot of custom features *wink wink*"

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix = '.', description = description, intents = intents,case_insensitive=True)



@bot.event
async def on_ready():
	print('------------')	
	print('Logged in as : ')
	print(bot.user.name)
	print(bot.user.id)
	print('------------')

@bot.command()
async def roll(ctx):
	#Rolls a Dice
	
	result = str(random.randint(1,6))
	await ctx.send(result)

@bot.command()
async def doge(ctx):
	img = 'images/doge.jpg'
	colorThis = colorEmbed[random.randint(0,len(colorEmbed)-1)]
	embed = discord.Embed(title="Doge the cool doeg", description="Such Badge, so wow", color=colorThis)
	file = discord.File(img, filename="image.jpg")
	embed.set_image(url="attachment://image.jpg")
	await ctx.send(file=file, embed=embed) 

	
@bot.command()
async def nish(ctx):
	finalList = finalNishList
	randomPost = finalList[random.randint(0, len(finalList)-1)]
	colorThis = colorEmbed[random.randint(0,len(colorEmbed)-1)]
	embed = discord.Embed(title="Nish's Post", description=randomPost["caption"], color=colorThis) #creates embed
	img = 'nishPhotos/' +  randomPost["image"] + '.jpg'
	file = discord.File(img, filename="image.jpg")
	embed.set_image(url="attachment://image.jpg")
	await ctx.send(file = file, embed=embed) 

@bot.command()
async def skwi(ctx, message:typing.Optional[str] = "existence"):
	print(message)
	embed = discord.Embed(title="Skwi's Answer", description="I reject your " + message.title(), color=0x00ff00) #creates embed
	imagePath = "skwiData/reject.gif"
	listMessage = message.split() 
	for i in listMessage:
		if i in finalSkwiList[0]:
			imagePath = finalSkwiList[1][finalSkwiList[0].index(i)]
			print(imagePath)
	file = discord.File(imagePath, filename="skwi.gif")
	embed.set_image(url="attachment://skwi.gif")
	await ctx.send(file = file, embed=embed) 

@bot.command()
async def summer(ctx,*, message:typing.Optional[str] = "pspsppspspsp"):
	print(message)
	finalMessage = ""
	if message == "pspsppspspsp":
		finalMessage = message
	else:
		finalMessage = checkSummer(message)
		
	embed = discord.Embed(title="Summer's response", description = finalMessage, color=0xbd7eea)
	embed.set_author(name = "Summer", icon_url="https://i.imgur.com/EIpCTtk.png")
	await ctx.send(embed = embed)

@bot.command(name = 'yazzy', aliases = ['nimnim','nimmy','yimyim'])
async def yazzy(ctx,*, imgCom: typing.Optional[str] = "default"):
	if imgCom not in YimYimIndexes:
		imgCom = "default" 
	img = getNimArts(imgCom)
	if imgCom.lower().strip() == "default":
		embed = discord.Embed(title="Yazzy aka Nimnim", description = "Let me teach you the way to enter a chat with style", color=0x4f9cef)
	elif imgCom.lower().strip() == "attac":
		embed = discord.Embed(title="Yazzy aka Nimnim", description = "You better be ready to feel some pain", color=0xe52239)
	elif imgCom.lower().strip() == "welcome":
		embed = discord.Embed(title="Yazzy aka Nimnim", description = "We welcome you to our Family", color=0xe273c7)
	else:
		embed = discord.Embed(title="Yazzy's Art", description = "This is how Yazzy drew her french " + imgCom.title() , color=0x5beaa7)
	embed.set_image(url = img)
	await ctx.send(embed = embed)

@bot.command(name = 'commands', aliases = ['cmd','command'] )
async def commands(ctx,*, helpCom: typing.Optional[str] = "all"):
	embed = discord.Embed(title="Help Desk Here, featuring Nurse Mami UwU", description = "Here you'll find everything you need to find about the Bot. Something may be hidden here though, so have a sharp eye OwO", color=0x4f9cef)
	await ctx.send(embed = embed)

@bot.command(name = 'member', aliases = ['members'])
async def member(ctx,*, member:typing.Optional[str] = "all"):
	
	if member == "all":
		embed = discord.Embed(title = "Members", description = "Here's a list of members whose info has been added in the bot ",color=0x4f9cef)
		for i in MembersList:		
			listM = getMembers(i)
			embed.add_field(name = i , value = listM[1], inline = False)
	else:
		k = getMembers(member)
		if k != False:
			embed = discord.Embed(title = member.title().strip(), description = k[1],color=0x4f9cef)
			embed.set_image(url = k[0])
		else:
			embed = discord.Embed(title = "Members", description = "You gave a member that does not exist in the Database. Try again with these members >.<",color=0x4f9cef)
			for i in MembersList:		
				listM = getMembers(i)
				embed.add_field(name = i , value = listM[1], inline = False)
	embed.set_footer(text="Information requested by: {}".format(ctx.author.display_name))
	await ctx.send(embed = embed)	

@bot.command(name = 'amanditis', aliases = ['amanda', 'adnama'])
async def amanditis(ctx,*, arg:typing.Optional[str] = "all"):
	if arg == "all":
		message = """**A·mand·a·it·is**
			/äman, dˈä-ˈīdəs/
			*noun*
			**noun: amandaitis**

				a severe condition of not being able to spell right with supposed illegible typing 
					*"Padma has amandaitis."*

			**Symptoms include**: *lack of grammar, switching up letters, and repeating of one word in different spellings*
			**Treatment**: *No known treatments have yet been discovered, but to make it better patients should use **slower typing**, look over message, and **use grammarly if possible***.
			
			||Info Provided by the Amazing Donutelli||
			"""
		await ctx.send(message)
	else:
		newMes = amandify(arg)
		await ctx.send(newMes)

@bot.command(name = 'hayafy', aliases = ['haya', 'hays'])
async def hayafy(ctx,*, arg:typing.Optional[str] = "all"):
	if arg == "all":
		message = """This disease have the symptoms of using a large amounts of unconnected yet strangely related emotes in a single sentence"""
		message = hayafying(message)
		await ctx.send(message)
	else:
		newMes = hayafying(arg)
		await ctx.send(newMes)

bot.run('ODEyNTcwMTEzNTE2NTAzMDgx.YDCq4w.MH34cXdLjh4b-HzhLVhCIKAEiMo')
