from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from discord.ext import commands
import discord
from datetime import datetime

token = "ODQ0MDA2NDUyNzk2NzE5MTc1.YKMIQw.98Pqzj1h2LwdeFiB0hc-31vqFPA"
bot = commands.Bot(command_prefix="!")
hotone = "ATTENTION BAJORAN WORKERS\r\nIT SURE IS A HOT ONE TODAY, HUH?"
mods = 805227140060676169

@bot.command()
async def giles(ctx):
    embed = discord.Embed(
        title="TestBotFart Commands",
        description="All bot commands listed below",
        color=discord.Color.blurple(),
        author="Dave"
    )
    embed.set_thumbnail(url="https://i.imgur.com/H0cnKwL.jpg")
    embed.add_field(name="!giles", value="List all commands", inline=False)
    embed.add_field(name="!clear - *date", value="Clears messages before a specified date", inline=False)
    embed.add_field(name="!ban", value="Bans a user", inline=False)
    embed.add_field(name="!unban *user", value="Unbans a user", inline=False)
    embed.add_field(name="!hotone", value="Displays a Hot One", inline=False)
    await ctx.send(embed=embed)


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
    



@bot.event
async def on_ready():
    ctx = discord.ctx
    hotone(ctx)
    scheduler = AsyncIOScheduler()

    scheduler.add_job(sendMessage, CronTrigger(month='1-12', day='*', hour=20, minute=00))

    scheduler.start()


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
        
        
@bot.command()
async def addrole(ctx, role: discord.Role, member: discord.Member=None):
    member = member or ctx.message.author
    await client.add_roles(member, role)
    await ctx.send(f"{str(member.name)} just added the {role} ")`
   
 
@addrole.error
async def addrole_error(ctx, error):
    if isinstance(error, commands.checkFailure):
        await ctx.send("You don't have permission, numbnuts")


bot.run(token)
