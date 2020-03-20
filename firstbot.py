from telegram.ext import Updater, MessageHandler, Filters, InlineQueryHandler
import logging
from telegram.ext import CommandHandler
import requests
import re

def start(incoming, outgoing):
    outgoing.bot.send_message(chat_id=incoming.effective_chat.id, text="Your wish is my Command!")

def echo(incoming, outgoing):
    chat_id = incoming.effective_chat.id
    text = incoming.message.text
    if text == "Hello There":
        outgoing.bot.send_message(chat_id = chat_id, text = "General Kenobi!")
    elif text == "What do we say to the God of Death?":
        outgoing.bot.send_message(chat_id = chat_id, text = "Not Today...")
    else:
        outgoing.bot.send_message(chat_id=chat_id, text="I am not really supposed to talk to you. Try sending me commands.")

def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url

def get_image_url():
    allowed_extension = ['jpg','jpeg','png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_url()
        file_extension = re.search("([^.]*)$",url).group(1).lower()
    return url

def dog(incoming, outgoing):
    url = get_image_url()
    chat_id = incoming.effective_chat.id
    outgoing.bot.send_photo(chat_id = chat_id, photo = url)

def photo_handler(incoming, outgoing):
    chat_id = incoming.effective_chat.id
    outgoing.bot.send_message(chat_id = chat_id, text = "Lets Solve this Sudoku!")
    

def main():
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    updater = Updater(token='804669526:AAEOQ2Vnp-nyfFZrM61vdVv74aTocNMFgA0', use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('dog',dog))

    dispatcher.add_handler(MessageHandler(Filters.text, echo))
    dispatcher.add_handler(MessageHandler(Filters.photo, photo_handler))
    
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()