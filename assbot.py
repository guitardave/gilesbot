# ASSBOT.PY free for use
# * DC 5/18/2021 v 0.1 - first release announces calls user "DUMBASS" on comment-edit and
#   says "HELLO" to me; also responds with dog emoji when user types "harf"
# * DC 5/19/2021 v 0.2 - adding a few basic commands (hello, fuckoff, hotone)
from datetime import datetime
from discord.ext import commands
import discord

token = "ODQ0MjU1MDQ5ODAxNzkzNTg2.YKPvyQ.TyzDge3ms892_3j3EJTi5vLfFuM"

bot = commands.Bot(command_prefix='!')

bot.remove_command('help')

@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title="BUTTER-BOT Commands",
        description="All bot commands listed below",
        color=discord.Color.blurple(),
        author="Dave"
    )
    embed.set_thumbnail(url="https://i.imgur.com/H0cnKwL.jpg")
    embed.add_field(name="!help", value="List all commands", inline=False)
    embed.add_field(name="!hello", value="Sends a hello message", inline=False)
    embed.add_field(name="!bashir", value="Displays a Bating Bashir", inline=False)
    embed.add_field(name="!what", value="Says 'What back, Poonspoon?'", inline=False)
    embed.add_field(name="!hotone", value="Displays HOT ONE", inline=False)
    embed.add_field(name="!harf", value="Displays Louis the Yellow Dog", inline=False)
    embed.add_field(name="!fuckoff [user]", value="Sends a fuckoff message to string specified", inline=False)
    await ctx.send(embed=embed)

@help.error
async def help_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You don't have permission to use this command")

@bot.command()
async def hello(ctx):
    await ctx.send("Hello, " + str(ctx.author))

@hello.error
async def hello_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You don't have permission to use this command")

@bot.command()
async def fuckoff(ctx, arg1=None):
    if arg1 == None:
        await ctx.send("You have to tell someone to fuckoff...")
    else:
        await ctx.send(str(ctx.author) + " is telling " + str(arg1) + " to FUCKOFF")
@fuckoff.error
async def fuckoff_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You don't have permission to use this command")

@bot.command()
async def bashir(ctx):
    embed = discord.Embed(
        title="Bating Bashir",
        color=discord.Color.blurple(),
        author="Dave"
    )
    embed.set_image(url="https://i.imgur.com/H0cnKwL.jpg")
    await ctx.send(embed=embed)
@bashir.error
async def bashir_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You don't have permission to use this command")

@bot.command()
async def what(ctx):
    await ctx.send("What back, Poonspoon!")
@what.error
async def what_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You don't have permission, numbnuts")

@bot.command()
async def hotone(ctx):
    embed = discord.Embed(
        title="Hot One",
        description="Attention Bajoran Workers, it sure is a Hot One today, huh?",
        color=discord.Color.dark_gold(),
        author="Dave"
    )
    embed.set_image(url="https://i.imgur.com/Zes8WN5.jpg")
    await ctx.send(embed=embed)
@hotone.error
async def hotone_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You don't have permission, numbnuts")

@bot.command()
async def harf(ctx):
    embed = discord.Embed(
        title="Harf!",
        color=discord.Color.blurple(),
        author="Dave"
    )
    embed.set_image(url="https://i.imgur.com/IlhLUSI.jpg")
    await ctx.send(embed=embed)
@harf.error
async def harf_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You don't have permission, numbnuts")


### ROLES 5/29/2021 DC
@bot.command()
async def ore(ctx):
    role = discord.utils.get(guild.roles, name="Ore Processors")
    await payload.member.add_roles(role)
    await ctx.send(str(member.name) +  " just added the Ore Processsors Role")
@ore.error
async def ore_error(ctx, error):
    if isinstance(error, commands.checkFailure):
        await ctx.send("You don't have permission, numbnuts")

bot.run(token)

