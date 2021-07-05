from cogs.translation_cog import translate_sent_message
from guild_manager import reset_all_guild_settings
import keep_alive

from discord.ext import commands

import os

PREFIX = '<3'

bot = commands.Bot(command_prefix=PREFIX)

@bot.event
async def on_ready():
  print('Logged in as {0.user}'.format(bot))

bot.load_extension("cogs.guild_settings_cog")
bot.load_extension("cogs.join_guild_cog")

@bot.event
async def on_message(message):
  if message.author == bot.user: 
    return
  if message.content.startswith(PREFIX):
    return await bot.process_commands(message)
  await translate_sent_message(message)

keep_alive.keep_alive()
bot.run(os.environ['TOKEN'])