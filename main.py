import os
from discord.ext import commands
from database_manager import *

PREFIX = '<'

bot = commands.Bot(command_prefix=PREFIX)

@bot.event
async def on_ready():
  print('Logged in as {0.user}'.format(bot))

@bot.event
async def on_guild_join(guild):
  print('Joined guild: ' + guild.id)

@bot.event
async def on_member_join(member):
  create_user(member.id)

@bot.event
async def on_message(message):
  if message.author == bot.user: 
    return
  if message.content.startswith(PREFIX):
    return await bot.process_commands(message)

bot.run(os.environ['TOKEN'])