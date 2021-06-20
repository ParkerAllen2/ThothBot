from replit import db

#guild_id = [probability, can delete, admin role]

def add_guild(guild_id):
  db[guild_id] = [100, False, guild_id]

def has_guild(guild_id):
  if(db[guild_id] == None):
    add_guild(guild_id)

def get_probability(guild_id):
  return db[guild_id][0]

def set_probability(guild_id, value):
  temp = db[guild_id]
  temp[0] = value
  db[guild_id] = temp

def can_delete(guild_id):
  return db[guild_id][1]

def set_can_delete(guild_id, value):
  temp = db[guild_id]
  temp[1] = value
  db[guild_id] = temp

def get_admin_role(guild_id):
  return db[guild_id][2]

def set_admin_role(guild_id, value):
  temp = db[guild_id]
  temp[2] = value
  db[guild_id] = temp

def has_admin_role(guild_id, author):
  if get_admin_role(guild_id) in [y.id for y in author.roles]:
    return True
  return False