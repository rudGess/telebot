import telebot
import config

tb = telebot.TeleBot(config.TOKEN_BOT)

def send_messege(message):
    tb.send_message(config.CHAT_ID,message)

@tb.message_handler(commands = ['start','help'])
def send_welcome(message):
    tb.reply_to(message,'Hi,hello')

@tb.message_handler(func=lambda message: True)
def echo_all(message):
    tb.reply_to(message,message.text)

#send_messege('I work')

tb.infinity_polling()


