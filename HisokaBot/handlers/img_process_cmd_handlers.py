from HisokaBot.funcs.imgProcess import *
from telegram import Update
from telegram.ext import CallbackContext
import shutil


def get(update: Update, context: CallbackContext):
    try:
        pfp = update.message.reply_to_message.from_user.get_profile_photos(
        ).photos[0][0].get_file().download()
        shutil.move(pfp, "funcs/pfp/file_1.jpg")
        pfp = update.message.from_user.get_profile_photos(
        ).photos[0][0].get_file().download()
        shutil.move(pfp, "funcs/pfp/file_0.jpg")
    except AttributeError:
        update.message.reply_text("Reply to an User!")


def drake(update: Update, context: CallbackContext) -> None:
    get(update, context)
    drake_meme()
    update.message.reply_photo(open('output.jpg', 'rb'))
    os.remove('output.jpg')


def slap(update: Update, context: CallbackContext) -> None:
    get(update, context)
    batman_slap()
    update.message.reply_photo(open('output.jpg', 'rb'))
    os.remove('output.jpg')


def shit(update: Update, context: CallbackContext) -> None:
    get(update, context)
    ew_stepped_in_shit()
    update.message.reply_photo(open('output.jpg', 'rb'))
    os.remove('output.jpg')


def cat(update: Update, context: CallbackContext) -> None:
    get(update, context)
    woman_yelling_at_cat()
    update.message.reply_photo(open('output.jpg', 'rb'))
    os.remove('output.jpg')


def forme(update: Update, context: CallbackContext) -> None:
    get(update, context)
    is_for_me()
    update.message.reply_photo(open('output.jpg', 'rb'))
    os.remove('output.jpg')


def butterfly(update: Update, context: CallbackContext) -> None:
    get(update, context)
    is_that_butterfly()
    update.message.reply_photo(open('output.jpg', 'rb'))
    os.remove('output.jpg')


def bruh(update: Update, context: CallbackContext) -> None:
    get(update, context)
    angry_pakistan_fan()
    update.message.reply_photo(open('output.jpg', 'rb'))
    os.remove('output.jpg')


def strong(update: Update, context: CallbackContext) -> None:
    get(update, context)
    strong_doge_weak_doge()
    update.message.reply_photo(open('output.jpg', 'rb'))
    os.remove('output.jpg')


def weak(update: Update, context: CallbackContext) -> None:
    get(update, context)
    weak_doge()
    update.message.reply_photo(open('output.jpg', 'rb'))
    os.remove('output.jpg')


def fact(update: Update, context: CallbackContext) -> None:
    get(update, context)
    facts_book()
    update.message.reply_photo(open('output.jpg', 'rb'))
    os.remove('output.jpg')


def aa(update: Update, context: CallbackContext) -> None:
    cxt = " ".join(context.args)
    htv_aliens_guy(cxt)
    update.message.reply_photo(open('output.png', 'rb'), quote=False)
    os.remove('output.png')
