from aiogram import types
from loader import dp

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    # Lotin-Kirill tarjimoni yozing
    translated_text = translate_function(message.text)

    # Lotin-Kirill tarjimoni qaytarish
    bot.reply_to(message, translated_text)