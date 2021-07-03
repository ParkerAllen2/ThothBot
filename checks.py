from discord.ext import commands
from services.guild_settings_service import find

def check_bot_edit_permission():
  async def predicate(ctx):
    guild_id = ctx.guild.id
    role_name = find(guild_id).bot_edit_role

    if role_name == "all":
      return True

    for author_role in ctx.author.roles:
      if author_role.name == role_name:
        return True
        
    return False
  return commands.check(predicate)

