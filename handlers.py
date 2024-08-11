from config import bot


@bot.message_handler(commands=['start'])
def start(text):
    bot.send_message(text.chat.id, 'Привет!')
