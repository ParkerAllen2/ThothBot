import uwuify
from owotext import OwO
import os
import discord
import random
from discord.ext import commands
import keep_alive
import guild_manager

bot = commands.Bot(command_prefix = '<3')
owo = OwO()
probability = 100
canDeleteOriginal = False

@bot.event
async def on_ready():
  print('We have logged in as {0.user}'.format(bot))

@bot.event
async def on_guild_join(guild):
  guild_manager.add_guild(guild.id)
  message = "BEHOLD! I have arrived to bring a curse upon this land. With this curse I will randomly translate your words into the sacred language. To learn more type "
  mes = owo.translate(message)
  mes = mes + "\"<3help\""
  
  for channel in guild.text_channels:
    if channel.permissions_for(guild.me).send_messages:
      await channel.send(mes)
      break

@bot.event
async def on_message(message):
  if message.author == bot.user:
    return
    
  g_id = message.guild.id
  guild_manager.has_guild(g_id)

  if message.content.startswith('<3'):
    await bot.process_commands(message)
    return

  if message.content.endswith('<3') or random.randint(0, guild_manager.get_probability(g_id)) == 0:
    #mes = uwuify.uwu(message.content)
    mes = owo.translate(message.content)

    mes = ">>> " + mes

    if guild_manager.can_delete(g_id):
      await message.delete()

    await message.channel.send(mes)
    await message.channel.send("~" + str(message.author.display_name) + " <3")

@bot.command(
name = "prob",
help = "Ex. <3prob 100 -Changes the probability to uwuify a message."
)
async def change_probability (ctx, prob):
  if not guild_manager.has_admin_role(ctx.guild.id, ctx.author):
    return
  
  g_id = ctx.guild.id
  try:
    guild_manager.set_probability(g_id, int(prob))
    await ctx.channel.send("Probability changed to 1 : " + str(prob))
  except ValueError:
    await ctx.channel.send("I require a whole number prarameter ex. <3prob 100")

@bot.command(
name = "del",
help = "Ex. <3del -Changes between letting the bot to delete the original message and send the uwuified message or just send a uwuified message."
)
async def delete_original (ctx):
  g_id = ctx.guild.id
  if not guild_manager.has_admin_role(g_id, ctx.author):
    return
  
  if guild_manager.can_delete(g_id):
    guild_manager.set_can_delete(g_id, False)
    await ctx.channel.send("Dose not delete original message")
  else:
    guild_manager.set_can_delete(g_id, True)
    await ctx.channel.send("Now deletes original message")

@bot.command(
name = "admin",
help = "Ex. <3admin [role name] -Set the role that can change the settings."
)
async def change_admin_role (ctx, role_name):
  g_id = ctx.guild.id
  if not guild_manager.has_admin_role(g_id, ctx.author):
    return
    
  for role in ctx.guild.roles:
    if role.name == role_name:
      guild_manager.set_admin_role(g_id, role.id)
      await ctx.channel.send(role_name + " is now my new master")
      return
  
  await ctx.channel.send("You do not have a role named " + role_name)

@bot.command(
name = "settings",
help = "Ex. <3settings -Returns your server settings"
)
async def view_settings (ctx):
  g_id = ctx.guild.id
  prob = guild_manager.get_probability(g_id)
  cand = guild_manager.can_delete(g_id)
  for role in ctx.guild.roles:
    if role.id == guild_manager.get_admin_role(g_id):
      admin = role.name
      break

  await ctx.channel.send(">>> Probability: " + str(prob) + "\nDeletes comment: " + str(cand) + "\nAdmin role: " + admin)

keep_alive.keep_alive()
bot.run(os.getenv('TOKEN'))