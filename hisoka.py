from telegram import Update, ParseMode
import shutil
import os
from imgProcess import *
from telegram.ext import Updater, CommandHandler, Dispatcher, CallbackContext

def get(update,context):
    try:
        pfp = update.message.reply_to_message.from_user.get_profile_photos().photos[0][0].get_file().download()
        shutil.move(pfp,"pfp/file_1.jpg")
        pfp = update.message.from_user.get_profile_photos().photos[0][0].get_file().download()
        shutil.move(pfp,"pfp/file_0.jpg")
    except AttributeError:
        update.message.reply_text("Reply to an User!")

def drake(update:Update,context:CallbackContext)->None:
    get(update,context)
    drake_meme()
    update.message.reply_photo(open('output.jpg', 'rb'))
    os.remove('output.jpg')

def slap(update:Update,context:CallbackContext)->None:
    get(update,context)
    batman_slap()
    update.message.reply_photo(open('output.jpg', 'rb'))
    os.remove('output.jpg')
    
def shit(update:Update,context:CallbackContext)->None:
    get(update,context)
    ew_stepped_in_shit()
    update.message.reply_photo(open('output.jpg', 'rb'))
    os.remove('output.jpg')

def cat(update:Update,context:CallbackContext)->None:
    get(update,context)
    woman_yelling_at_cat()
    update.message.reply_photo(open('output.jpg', 'rb'))
    os.remove('output.jpg')

def forme(update:Update,context:CallbackContext)->None:
    get(update,context)
    is_for_me()
    update.message.reply_photo(open('output.jpg', 'rb'))
    os.remove('output.jpg')
    
def butterfly(update:Update,context:CallbackContext)->None:
    get(update,context)
    is_that_butterfly()
    update.message.reply_photo(open('output.jpg', 'rb'))
    os.remove('output.jpg')

def bruh(update:Update,context:CallbackContext)->None:
    get(update,context)
    angry_pakistan_fan()
    update.message.reply_photo(open('output.jpg', 'rb'))
    os.remove('output.jpg')

def strong(update:Update,context:CallbackContext)->None:
    get(update,context)
    strong_doge_weak_doge()
    update.message.reply_photo(open('output.jpg', 'rb'))
    os.remove('output.jpg')

def weak(update:Update,context:CallbackContext)->None:
    get(update,context)
    weak_doge()
    update.message.reply_photo(open('output.jpg', 'rb'))
    os.remove('output.jpg')

def fact(update:Update,context:CallbackContext)->None:
    get(update,context)
    facts_book()
    update.message.reply_photo(open('output.jpg', 'rb'))
    os.remove('output.jpg')

def commands(update:Update,context:CallbackContext)->None:
    update.message.reply_text("<pre>/slap</pre>\n<pre>/drake</pre>\n<pre>/cat</pre>\n<pre>/forme</pre>\n<pre>/butterfly</pre>\n<pre>/fact</pre>\n<pre>/weak</pre>\n<pre>/strong</pre>\n<pre>/bruh</pre>\n<pre>/commands</pre>",parse_mode = 'HTML')



if __name__ == "__main__":
    
    bot_token = os.environ.get("BOT_TOKEN","")
    updater = Updater(bot_token,use_context = True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("drake",drake,run_async = True))
    dp.add_handler(CommandHandler("slap",slap,run_async = True))
    dp.add_handler(CommandHandler("shit",shit,run_async = True))
    dp.add_handler(CommandHandler("cat",cat,run_async = True))
    dp.add_handler(CommandHandler("forme",forme,run_async = True))
    dp.add_handler(CommandHandler("butterfly",butterfly,run_async = True))
    dp.add_handler(CommandHandler("fact",fact,run_async = True))
    dp.add_handler(CommandHandler("weak",weak,run_async = True))
    dp.add_handler(CommandHandler("strong",strong,run_async = True))
    dp.add_handler(CommandHandler("bruh",bruh,run_async = True))
    dp.add_handler(CommandHandler("availCommands",commands,run_async = True))

    updater.start_polling()
    updater.idle()
