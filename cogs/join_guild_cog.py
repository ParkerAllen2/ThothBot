from discord.ext import commands

from services.guild_settings_service import add
from services.join_guild_service import get_join_guild_embed

from check.bot_edit_permission import check_bot_edit_permission, no_permission


class join_guild_cog(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    
  @commands.Cog.listener()
  async def on_guild_join(self, guild):
    add(guild.id)
    bot_name = "Θώθ, Lord of the Sacred Words"
    await self.bot.user.edit(nick=bot_name)
    content = get_join_guild_embed(bot_name)
    
    for channel in guild.text_channels:
      if channel.permissions_for(guild.me).send_messages:
        await channel.send(embed=content)
        break

  @commands.command(
    name = 'display_join_message',
    aliases = ['join_message', 'join'],
    help = 'Display the initial join guild message'
  )
  @check_bot_edit_permission()
  async def display_join_message(self, ctx):
    await ctx.message.delete(delay = 1)
    content = get_join_guild_embed(self.bot.user.display_name)
    await ctx.send(embed=content)
  
  async def cog_command_error(self, ctx, error):
    await ctx.message.delete(delay = 1)
    if isinstance(error, no_permission):
      await ctx.send(error, delete_after=5) 


def setup(bot):
  bot.add_cog(join_guild_cog(bot))