import discord
import random
import datetime
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
from mcstatus import MinecraftServer
import colorama
#-- By: Gábor. Discord: Gábor#0001
colorama.init()

bot = commands.Bot(command_prefix='!')
token = 'NTcwOTU4MTI2NDg1MDc4MDM2.XMGwVw.NhA63F9k_i9m8KCoFO3c0W2z2T4'
bot.remove_command('help')


@bot.event
async def on_ready():
	ido = datetime.datetime.now().strftime("%H:%M:%S")
	print("[\u001b[96m",ido,"\u001b[0m]","VoxelGamesBOT \u001b[92mElindult\u001b[0m")
	print("[\u001b[96m",ido,"\u001b[0m]","VoxelGamesBOT Verzió:\u001b[92m v0.1 \u001b[0m")
	print("")
	await bot.edit_channel(bot.get_channel("570954994795282452"),name="Játékosok: " + str(MinecraftServer.lookup("play.voxelgames.net:25565").status().players.online))
	print("")
	await bot.change_presence(game=discord.Game(name="play.voxelgames.net", type = 1))

#-- Probléma PARANCS INNENTŐL --
@bot.command(pass_context=True)
@commands.cooldown(1, 600, commands.BucketType.user) #10perc = 600
async def help(ctx, *phrase):
	if ctx.message.channel.id == "467409504733233154":
		problema = ''
		if len(phrase) != 0:
			for word in phrase:
				problema += word
				problema += " "
		else:
				problema = "Nincs megadva probléma"
		await bot.send_message(ctx.message.author, "A problémád sikeresen továbbítva az adminoknak pár percen belül választ kapsz a problémádra tőlük!")
		await bot.delete_message(ctx.message)
		ido = datetime.datetime.now().strftime("%H:%M:%S")
		print("[\u001b[96m",ido,"\u001b[0m] Új probléma létrehozva általa " + str(ctx.message.author) + " probléma: " + str(problema))
		embed = discord.Embed(title="VoxelGamesBOT | Probléma", description="\nJátékos neve: " + str(ctx.message.author) + "\n" + "\nProbléma: " + str(problema), color=0x0000ff, timestamp=datetime.datetime.now())
		embed.set_footer(text="VoxelGamesBOT v0.1 By: Gábor.")
		role = discord.utils.get(ctx.message.server.roles, name="Admin")
		for member in ctx.message.server.members:
			if role in member.roles:
				await bot.send_message(member, embed=embed)
	else:
		await bot.say("Ebben a channel-ban nem használhatod ezt a paracsot!")

#-- By: Gábor. Discord: Gábor#0001

@help.error
async def help_error(error, ctx):
	if isinstance(error, commands.CommandOnCooldown):
		embed = discord.Embed(title="VoxelGamesBOT | Hiba", description='A parancsot nem tudod használni még {:.2f}mp-ig.'.format(error.retry_after), color=0xff0000, timestamp=datetime.datetime.now())
		embed.set_footer(text="VoxelGamesBOT v0.1 By: Gábor.")
		await bot.send_message(ctx.message.author, embed=embed)
	else:
		raise error
# -- Probléma PARANCS VÉGE --

async def lekerdezes():
	await bot.wait_until_ready()
	counter = 0
	while not bot.is_closed:
		counter += 1
		await bot.edit_channel(bot.get_channel("570954994795282452"),name="Játékosok: " + str(MinecraftServer.lookup("play.voxelgames.net:25565").status().players.online))
		ido = datetime.datetime.now().strftime("%H:%M:%S")
		print("[\u001b[96m",ido,"\u001b[0m]", "Channel Frissítve, játékosok: " + str(MinecraftServer.lookup("play.voxelgames.net:25565").status().players.online) + " következő frissítés 1perc múlva")
		await asyncio.sleep(60) # 1percenként (60mp)

# <--- Bot Run --->
bot.loop.create_task(lekerdezes())
bot.run(token)

#-- By: Gábor. Discord: Gábor#0001