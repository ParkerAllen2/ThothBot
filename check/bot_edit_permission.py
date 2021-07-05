from discord.ext import commands
from services.guild_settings_service import find

def check_bot_edit_permission():
  async def predicate(ctx):
    guild_id = ctx.guild.id
    role_name = find(guild_id).bot_edit_role

    if role_name == "all" or role_name == "everyone":
      return True

    for author_role in ctx.author.roles:
      if author_role.name == role_name:
        return True
        
    raise no_permission("Missing permissions to edit bot settings")

  return commands.check(predicate)

class no_permission(commands.CheckFailure):
  pass