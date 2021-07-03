class guild_settings:
  def __init__(self, guild_id, bot_edit_role, translation_probability, can_delete):
    self.guild_id = guild_id
    self.bot_edit_role= bot_edit_role
    self.translation_probability = translation_probability
    self.can_delete = can_delete
  