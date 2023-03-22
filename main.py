#importing packages and discord bots to get the program running
import discord, os
import random
from discord.ext import commands
from jokeapi import Jokes

#token for the discord botT
TOKEN = os.environ['TOKEN']

intents = discord.Intents.default()
intents.message_content = True

#the prefix used before command for the command to work
bot = commands.Bot(command_prefix="!", intents=intents)

#picking a random number for the user to guess
class rng:

  def __init__(self):
    self.secret_number = random.randint(0, 1000)

  def reset(self):
    self.secret_number = random.randint(0, 1000)


random_number = rng()

#code for user to correctly guess the mystery number giving hints to help them get closer
@bot.command(name="guess")
async def guess(ctx, num):
  if int(num) == random_number.secret_number:
    await ctx.channel.send("Moto Moto loves you <3")
    random_number.reset()
  elif int(num) > random_number.secret_number:
    await ctx.channel.send("Guess Lower monkey")
  else:
    await ctx.channel.send("Guess Higher monkey")


#this code is for a bot who tells jokes when the user asks
@bot.command()
async def joke(ctx: commands.Context):
  j = await Jokes()
  blacklist = ["racist"]
  if not ctx.message.channel.is_nsfw():
    blacklist.append("nsfw")
  joke = await j.get_joke(blacklist=blacklist)
  msg = ""
  if joke["type"] == "single":
    msg = joke["joke"]
  else:
    msg = joke["setup"]
    msg += f"||{joke['delivery']}||"
  await ctx.send(msg)


bot.run(TOKEN)
