from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from discord.ext import commands
import discord
from datetime import datetime

token = "ODQ0MDA2NDUyNzk2NzE5MTc1.YKMIQw.98Pqzj1h2LwdeFiB0hc-31vqFPA"
#token = "ODQ0MjU1MDQ5ODAxNzkzNTg2.YKPvyQ.TyzDge3ms892_3j3EJTi5vLfFuM"
client = discord.Client()
hotchan = 805220125585309716
#hotchan = 844006240992100404
hotone = "ATTENTION BAJORAN WORKERS\r\nIT SURE IS A HOT ONE TODAY, HUH?"


async def sendMessage():
    guild = client.get_channel(hotchan)
    await guild.send(hotone)

@client.event
async def on_ready():
    print("GILESBOT IS ONLINE at" + str(datetime.now()))
    scheduler = AsyncIOScheduler()

    scheduler.add_job(sendMessage, CronTrigger(month='1-12', day='*', hour=20, minute=00))

    scheduler.start()

client.run(token)
