import uwuify
from owotext import OwO

owo = OwO()

def translate_message(message):
  #mes = uwuify.uwu(message.content)
  mes = owo.translate(message)
  return mes