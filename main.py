import discord
import random
from discord.ext import commands

TOKEN = "MTA4MDk2MDkwNjgxMDM3NjMxMw.GkxzzA.7xhMBR2W0tKvDY7wuIb2OmMSJDzBDZQ9LDLy9k"

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix = "$", intents = intents)




bot.run(TOKEN)

"""
import os
import discord
import random
from discord.ext import commands

TOKEN = os.environ['TOKEN']
intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix="!", intents=intents)


class rng:

  def __init__(self):
    self.secret_number = random.randint(0, 1000)

  def reset(self):
    self.secret_number = random.randint(0, 1000)


random_number = rng()


@client.command(name="guess")
async def guess(ctx, num):
  if int(num) == random_number:
    await ctx.channel.send("Correct. I love you Finn Abey <3")
  elif int(num) > random_number.secret_number:
    await ctx.channel.send("Guess Lower")
  else:
    await ctx.channel.send("Guess Higher")


client.run(TOKEN)
"""