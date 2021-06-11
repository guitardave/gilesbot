import os
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!")
token = os.environ(DISCORD_TOKEN)
mods = 845859190424993853
bot.remove_command('help')

@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title="TestBotFart Commands",
        description="All bot commands listed below",
        color=discord.Color.blurple(),
        author="Dave"
    )
    embed.set_thumbnail(url="https://i.imgur.com/H0cnKwL.jpg")
    embed.add_field(name="!help", value="List all commands", inline=False)
    embed.add_field(name="!clear - *date", value="Clears messages before a specified date", inline=False)
    embed.add_field(name="!ban", value="Bans a user", inline=False)
    embed.add_field(name="!unban *user", value="Unbans a user", inline=False)
    embed.add_field(name="!hotone", value="Displays a Hot One", inline=False)
    embed.add_field(name="!harf", value="Displays a Louis Lewis", inline=False)
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount, month=None, day=None, year=None):
    if amount == "-":
        amount = None
    else:
        amount = int(amount) + 1
    if month == None or day == None or year == None:
        date = None
    else:
        date = datetime.datetime(int(year), int(month), int(day))

    await ctx.channel.purge(limit=amount, after=date)

@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You don't have permission to use this command")

@bot.command()
@commands.has_role(mods)
async def kick(ctx, member: discord.Member, *, reason):
    await member.kick(reason=reason)

@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You don't have permission to use this command")

@bot.command()
@commands.has_role(mods)
async def ban(ctx, member: discord.Member, *, reason):
    await member.ban(reason=reason)

@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You don't have permission to use this command")

@bot.command()
@commands.has_role(mods)
async def unban(ctx, *, member):
    banned_members = await ctx.guild.bans()
    for person in banned_members:
        user = person.user
        if member == str(user):
            await ctx.guild.unban(user)

@unban.error
async def unban_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You don't have permission to use this command")

#assbot test commands

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

@bot.command()
async def harf(ctx):
    embed = discord.Embed(
        title="Harf!",
        color=discord.Color.blurple(),
        author="Dave"
    )
    embed.set_image(url="https://i.imgur.com/IlhLUSI.jpg")
    await ctx.send(embed=embed)

@bot.command()
async def fuckoff(ctx, arg1=None):
    if arg1 == None:
        await ctx.send("You have to tell someone to fuckoff...")
    else:
        await ctx.send(str(ctx.author) + " is telling " + str(arg1) + " to FUCKOFF")

bot.run(token)