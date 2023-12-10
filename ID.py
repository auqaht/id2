import telebot

bot = telebot.TeleBot('6371146275:AAGQth_mr2COoBB9d_3RkkaYBu1Tqr0r1-s')

@bot.message_handler(commands=['start'])
def start(message):
    user = message.from_user
    
    text = f"Hello {user.first_name}!\n"
    text += f"• Your user ID: {user.id}\n"
    text += f"• Current chat ID: {message.chat.id}\n"
    text += "\n"
    text += "• By : @auq7t \n"
    text += "• My channel: https://t.me/DB0Ts"

    
    bot.send_message(message.chat.id, text)

bot.polling()
