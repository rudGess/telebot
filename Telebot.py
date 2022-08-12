import telebot
import config

tb = telebot.TeleBot(config.TOKEN_BOT)

def send_message(message):
    tb.send_message(config.CHAT_ID,message)

def test_message(message):
	return message.document.mime_type == 'text/plain'

@tb.message_handler(commands = ['start','help'])
def send_welcome(message):
    tb.reply_to(message,'Hi,hello')

@tb.message_handler(regexp = 'SOME_REGEXP')
def handle_message(message):
    pass

@tb.message_handler(content_types=['document', 'audio'])
def handle_docs_audio(message):
    pass

@tb.message_handler(func=lambda message: message.document.mime_type == 'text/plain', content_types=['document'])
def handle_text_doc(message):
	pass

@tb.message_handler(func=test_message, content_types=['document'])
def handle_text_doc(message):
	pass

@tb.message_handler(func=lambda message: True)
def echo_all(message):
    tb.reply_to(message,message.text)

tb.infinity_polling()


