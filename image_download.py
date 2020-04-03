import logging
import urllib.request
from telegram.ext import Updater, MessageHandler, Filters
 
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def some_func(incoming, update):
    photo = incoming.get_file(update.effective_message.photo[-1].file_id)
    filename = 'test.png'
    urllib.request.urlretrieve(photo["file_path"],filename)
        
def main():
    updater = Updater('<Enter the unique id here>')
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.all, some_func))
    updater.start_polling()
    updater.idle()
    
if __name__ == '__main__':
    main()
