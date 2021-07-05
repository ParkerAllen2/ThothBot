from replit import db
from services.guild_settings_service import add

#guild_id = [probability, can delete, admin role]
def reset_all_guild_settings():
  for key in db.keys():
    add(key)
  print("reset")

#reset_all_guild_settings()
