import discord, os
import random
from discord.ext import commands

TOKEN = os.environ['token']

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="$", intents=intents)


class rng:
  def __init__(self):
    self.secret_number = random.randint(0,1000)

  def reset(self):
    self.secret_number = random.randint(0,1000)

random_number = rng()

@bot.command(name="guess")
async def guess(ctx, num):
  if int(num) == random_number:
    await ctx.channel.send("Correct. I love you Finn Abey <3")
  elif int(num) > random_number.secret_number:
    await ctx.channel.send("Guess Lower")
  else:
    await ctx.channel.send("Guess Higher")




