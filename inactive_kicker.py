import os
import time

import discord #must install discord.py library. python3 -m pip install discord.py if you have not already done so.

TOKEN = os.getenv("INACTIVE_KICKER_TOKEN") #where INACTIVE_KICKER_TOKEN is an env variable. I simply have INACTIVE_KICKER_TOKEN="abc123" in .bashrc.
intents = discord.Intents.all() #needed for next line
client = discord.Client(intents=intents) #as of api v2.0 this is required

@client.event
async def on_voice_state_update(member, before, after):
    if before.channel is None and after.channel is not None and member.id == 123: #music bot id, can just get from right-clicking user in dev mode
        time.sleep(10800) #3 hours in seconds
        await member.edit(voice_channel=None)
        await member.guild.get_channel(456).send("<Music bot> has been disconnected due to inactivity!") #bot name, id of bot channel, can get in dev mode

client.run(TOKEN)
