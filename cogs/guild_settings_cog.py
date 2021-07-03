from discord.ext import commands
from checks import check_bot_edit_permission
from services.guild_settings_service import add, find, update, delete

class guild_settings_cog(commands.Cog):
  def _init_(self, bot):
    self.bot = bot

  @commands.command(
    name = 'display_settings',
    aliases = ['settings'],
    help = 'Displays my current settings'
  )
  async def display_settings(self, ctx):
    guild_id = ctx.guild.id
    guild_settings = find(guild_id)
    message = "settings\nbot editor role: " + guild_settings.bot_edit_role 
    + "\ntranslation probability: " + guild_settings.translation_probability
    + "\ncan delete original message: " + guild_settings.can_delete

    await ctx.send(message)

  @commands.command(
    name = 'bot_edit_role',
    aliases = ['bot_editor', 'edit_role'],
    help = 'Set the role you want to be able to adjust me'
  )
  @check_bot_edit_permission()
  async def set_bot_edit_role(self, ctx, role: commands.RoleConverter):
    guild_id = ctx.guild.id
    guild_settings = find(guild_id)
    guild_settings.bot_edit_role = role.name
    update(guild_id, guild_settings)

def setup(bot):
  bot.add_cog(guild_settings_cog(bot))