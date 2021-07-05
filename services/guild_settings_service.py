from replit import db
from model.guild_settings import guild_settings

def add(guild_id):
  settings = guild_settings(guild_id, "all", 20, False)
  db[guild_id] = map_to_dictionary(settings)
  return settings

def find(guild_id):
  settings = db[guild_id]
  if settings is None:
    settings = add(guild_id)
  return map_from_dictionary(settings)

def update(guild_id, settings):
  db[guild_id] = map_to_dictionary(settings)

def delete(guild_id):
  del db[guild_id]

def map_to_dictionary(settings):
  return {
    "guild_id": settings.guild_id,
    "bot_edit_role": settings.bot_edit_role,
    "translation_probability": settings.translation_probability,
    "can_delete": settings.can_delete
  }

def map_from_dictionary(settings):
  return guild_settings(
    settings["guild_id"],
    settings["bot_edit_role"],
    settings["translation_probability"],
    settings["can_delete"]
    )
