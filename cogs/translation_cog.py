from services.guild_settings_service import find
from services.translation_service import translate_message

import random
import discord

async def translate_sent_message(message):
  guild_id = message.guild.id
  guild_settings = find(guild_id)

  content = message.content

  if not content.endswith('<3') and random.randint(0, guild_settings.translation_probability) != 0:
    return
  
  if guild_settings.can_delete:
    await message.delete(delay = 1)

  content = translate_message(content)
  footer = "~{}<3".format(message.author.display_name)

  embed = discord.Embed(title=content)
  embed.set_footer(text=footer)

  await message.channel.send(embed=embed)


