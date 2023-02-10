import logging
import telegram
from telegram.ext import Updater, MessageHandler , filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def welcome_message(update, context):
    if update.message.new_chat_members:
        for new_member in update.message.new_chat_members:
            username = new_member.username
            text = "Welcome @{} to the group! How can I help you today?".format(username)
            context.bot.send_message(chat_id=update.message.chat_id, text=text)

updater = Updater(token="6063844648:AAHAj364o8zfZHYQleg4wmFwiRvnaikFal0", use_context=True)
dispatcher = updater.dispatcher
welcome_handler = MessageHandler(Filters.status_update.new_chat_members, welcome_message)
dispatcher.add_handler(welcome_handler)

updater.start_polling()
