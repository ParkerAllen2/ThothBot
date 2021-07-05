from services.translation_service import translate_message

import discord

title = "BEHOLD!"
translated_title = translate_message(title)
description = "I have arrived to bring a curse upon this land. With this curse I will randomly translate your words into the sacred language. To learn more type "
translated_description = translate_message(description) + "\"<3help\""

embed = discord.Embed(title=translated_title, description = translated_description)

def get_join_guild_embed(bot_name):
  footer = "~{}<3".format(bot_name)

  embed.set_footer(text=footer)
  return embed