from telegram import Update,Bot
import shutil
import os
from telegram.ext import Updater,CommandHandler,Dispatcher,CallbackContext
from imgProcess import *




def quoteUserName(name):
    if len(name) > 10 and len(name) <= 25:
        name = name[:len(name)//2]+"\n"+name[len(name)//2:]
    else:
        name = name[:len(name)//3]+"\n"+name[(len(name)//3):(len(name)//3)+len(name)//3]+"\\n"+name[len(name)//3:]
    return name

def getpic(update:Update,context:CallbackContext)->None:
    try:
        index = 0
        user = update.message.from_user
        USERNAME = user['username']
        USERNAME = quoteUserName(USERNAME)
        user_pfp = user.get_profile_photos().photos[0][0]
        file = context.bot.get_file(user_pfp).download()
        shutil.move(file,f'pfp/file_{index}.jpg')
        index+=1
        quote = update.message.reply_to_message.from_user
        QUOTENAME = quote['username']
        QUOTENAME = quoteUserName(QUOTENAME)
        quote_pfp = quote.get_profile_photos().photos[0][0]
        file = context.bot.get_file(quote_pfp).download()
        shutil.move(file,f'pfp/file_{index}.jpg')
        index+=1
    except AttributeError:
        update.message.reply_text("Must reply to a User!")
    

def drake(update:Update,context:CallbackContext)->None:
    getpic(update,context)
    drake_meme()
    update.message.reply_photo(open('output.jpg', 'rb'))
    os.remove('output.jpg')

def slap(update:Update,context:CallbackContext)->None:
    getpic(update,context)
    batman_slap()
    update.message.reply_photo(open('output.jpg', 'rb'))
    os.remove('output.jpg')
    
def shit(update:Update,context:CallbackContext)->None:
    getpic(update,context)
    ew_stepped_in_shit()
    update.message.reply_photo(open('output.jpg', 'rb'))
    os.remove('output.jpg')

def cat(update:Update,context:CallbackContext)->None:
    getpic(update,context)
    woman_yelling_at_cat()
    update.message.reply_photo(open('output.jpg', 'rb'))
    os.remove('output.jpg')

def forme(update:Update,context:CallbackContext)->None:
    getpic(update,context)
    is_for_me()
    update.message.reply_photo(open('output.jpg', 'rb'))
    os.remove('output.jpg')
    
def butterfly(update:Update,context:CallbackContext)->None:
    getpic(update,context)
    is_that_butterfly()
    update.message.reply_photo(open('output.jpg', 'rb'))
    os.remove('output.jpg')


if __name__ == "__main__":
    
    bot_token = os.environ.get(BOT_TOKEN,"")
    updater = Updater(bot_token,use_context = True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("slap",slap,run_async = True))
    dp.add_handler(CommandHandler("drake",drake,run_async = True))
    dp.add_handler(CommandHandler("shit",shit,run_async = True))
    dp.add_handler(CommandHandler("cat",cat,run_async = True))
    dp.add_handler(CommandHandler("forme",forme,run_async = True))
    dp.add_handler(CommandHandler("butterfly",butterfly,run_async = True))

    updater.start_polling()
    updater.idle()
