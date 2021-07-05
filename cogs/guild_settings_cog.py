from discord.ext import commands

from check.bot_edit_permission import check_bot_edit_permission, no_permission
from check.missing_bot_settings import has_missing_settings, missing_settings
from services.guild_settings_service import add, find, update

class guild_settings_cog(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  
  
  @commands.command(
    name = 'display_settings',
    aliases = ['settings'],
    help = 'Displays my current settings'
  )
  async def display_settings(self, ctx):
    await ctx.message.delete(delay = 1)

    guild_id = ctx.guild.id
    guild_settings = find(guild_id)

    message = "Settings"
    message += "\nBot editor role: {}".format(guild_settings.bot_edit_role)
    message += "\nTranslation probability: {}".format(guild_settings.translation_probability)
    message += "\nDelete original message: {}".format(guild_settings.can_delete)

    await ctx.send(message, delete_after=10)

  @commands.command(
    name = 'bot_nickname',
    aliases = ['bot_nick', 'nick'],
    help = 'Change the nickname of the bot'
  )
  @check_bot_edit_permission()
  async def set_bot_nickname(self, ctx, bot_name):
    await ctx.message.delete(delay = 1)
    await self.bot.user.edit(nick=bot_name)

  @commands.command(
    name = 'bot_edit_role',
    aliases = ['bot_editor', 'edit_role'],
    help = 'Set the role you want to be able to adjust me'
  )
  @check_bot_edit_permission()
  async def set_bot_edit_role(self, ctx, role: commands.RoleConverter):
    await ctx.message.delete(delay = 1)
    
    guild_id = ctx.guild.id
    guild_settings = find(guild_id)
    guild_settings.bot_edit_role = role.name
    update(guild_id, guild_settings)

    await ctx.send("Bot edit permission -> {}".format(role.name), delete_after=5)


  @commands.command(
    name = 'translation_probability',
    aliases = ['probability', 'prob'],
    help = 'Set the probability to translate a message'
  )
  @check_bot_edit_permission()
  async def set_translation_probability(self, ctx, arg: int):
    await ctx.message.delete(delay = 1)

    if arg < 0:
      await ctx.send("Argument Error:\nThis commands requires a number greater than or equal to 0", delete_after=5)
      return
    
    guild_id = ctx.guild.id
    guild_settings = find(guild_id)
    guild_settings.translation_probability = arg
    update(guild_id, guild_settings)

    await ctx.send("Translation probability -> {}".format(arg), delete_after=5)

  
  @commands.command(
    name = 'delete_original',
    aliases = ['del_og', 'can_del'],
    help = 'Changes whether bot keeps or deletes the original message'
  )
  @check_bot_edit_permission()
  async def can_delete_original(self, ctx):
    await ctx.message.delete(delay = 1)
    
    guild_id = ctx.guild.id
    guild_settings = find(guild_id)
    can_delete = not guild_settings.can_delete
    guild_settings.can_delete = can_delete
    update(guild_id, guild_settings)

    await ctx.send("Delete original message -> {}".format(can_delete), delete_after=5)


  @commands.command(
    name = 'reset_settings',
    aliases = ['reset'],
    help = 'Reset the settings of the bot'
  )
  @check_bot_edit_permission()
  @has_missing_settings()
  async def reset_settings(self, ctx):
    await ctx.message.delete(delay = 1)

    guild_id = ctx.guild.id
    add(guild_id)
    await ctx.send("Server settings reset", delete_after=5)


  async def cog_command_error(self, ctx, error):
    await ctx.message.delete(delay = 1)
    if isinstance(error, missing_settings):
      await ctx.send(error, delete_after=5)
    if isinstance(error, no_permission):
      await ctx.send(error, delete_after=5) 

def setup(bot):
  bot.add_cog(guild_settings_cog(bot))