import telebot
import config

tb = telebot.TeleBot(config.TOKEN_BOT)

def send_messege(message):
    tb.send_message(config.CHAT_ID,message)

#tb.infinity_polling()


send_messege('https://pypi.org/project/pyTelegramBotAPI/#getting-started')
