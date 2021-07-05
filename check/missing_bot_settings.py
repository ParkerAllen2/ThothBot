from discord.ext import commands
from services.guild_settings_service import find

def has_missing_settings():
  async def predicate(ctx):
    guild_id = ctx.guild.id
    try:
      if find(guild_id) == None:
        return True
      raise missing_settings("Server is not missing settings")
    except:
      return True
    
  return commands.check(predicate)

class missing_settings(commands.CheckFailure):
  pass