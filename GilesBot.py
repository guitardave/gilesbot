from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from discord.ext import commands
import discord
from datetime import datetime
import os


token = os.environ.get('DISCORD_TOKEN')
client = discord.Client()
hotchan = '805220125585309716'


async def sendMessage():
    guild = client.get_channel(hotchan)
    await guild.send("ATTENTION BAJORAN WORKERS\r\nIT SURE IS A HOT ONE TODAY, HUH?")


@client.event
async def on_ready():
    print(f'GILESBOT IS ONLINE at {str(datetime.now())}')

    scheduler = AsyncIOScheduler()
    scheduler.add_job(sendMessage, CronTrigger(month='1-12', day='*', hour=20, minute=00))
    scheduler.start()

client.run(token)
