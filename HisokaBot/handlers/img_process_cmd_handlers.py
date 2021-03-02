from HisokaBot.funcs.imgProcess import *
from telegram import Update
from telegram.ext import CallbackContext
import shutil
from HisokaBot import logger


def get(update: Update, context: CallbackContext, cmd):
    try:
        pfp = update.message.reply_to_message.from_user.get_profile_photos(
        ).photos[0][0].get_file().download()
        shutil.move(pfp, "funcs/pfp/file_1.jpg")
        pfp = update.message.from_user.get_profile_photos(
        ).photos[0][0].get_file().download()
        shutil.move(pfp, "funcs/pfp/file_0.jpg")
    except AttributeError:
        update.message.reply_text("Reply to an User!")
        logger.info(msg=f"@{update.effective_user.username} /{cmd} [RTUI]")


def drake(update: Update, context: CallbackContext) -> None:
    cmd = 'drake'
    target = update.message.reply_to_message.from_user.username
    logger.info(msg=f"@{update.effective_user.username} did /drake to {target}")
    get(update, context, cmd)
    drake_meme()
    update.message.reply_photo(open('output.jpg', 'rb'))
    os.remove('output.jpg')
    logger.info(msg=f"@{update.effective_user.username} /{cmd} SUCCESSFULL")


def slap(update: Update, context: CallbackContext) -> None:
    cmd = 'slap'
    target = update.message.reply_to_message.from_user.username
    logger.info(msg=f"@{update.effective_user.username} did /slap to {target}")
    get(update, context, cmd)
    batman_slap()
    update.message.reply_photo(open('output.jpg', 'rb'))
    os.remove('output.jpg')
    logger.info(msg=f"@{update.effective_user.username} /{cmd} SUCCESSFULL")


def shit(update: Update, context: CallbackContext) -> None:
    cmd = 'shit'
    target = update.message.reply_to_message.from_user.username
    logger.info(msg=f"@{update.effective_user.username} did /shit to {target}")
    get(update, context, cmd)
    ew_stepped_in_shit()
    update.message.reply_photo(open('output.jpg', 'rb'))
    os.remove('output.jpg')
    logger.info(msg=f"@{update.effective_user.username} /{cmd} SUCCESSFULL")


def cat(update: Update, context: CallbackContext) -> None:
    cmd = 'cat'
    target = update.message.reply_to_message.from_user.username
    logger.info(msg=f"@{update.effective_user.username} did /cat to {target}")
    get(update, context, cmd)
    woman_yelling_at_cat()
    update.message.reply_photo(open('output.jpg', 'rb'))
    os.remove('output.jpg')
    logger.info(msg=f"@{update.effective_user.username} /{cmd} SUCCESSFULL")


def forme(update: Update, context: CallbackContext) -> None:
    cmd = 'forme'
    target = update.message.reply_to_message.from_user.username
    logger.info(msg=f"@{update.effective_user.username} did /forme to {target}")
    get(update, context, cmd)
    is_for_me()
    update.message.reply_photo(open('output.jpg', 'rb'))
    os.remove('output.jpg')
    logger.info(msg=f"@{update.effective_user.username} /{cmd} SUCCESSFULL")


def butterfly(update: Update, context: CallbackContext) -> None:
    cmd = 'butterfly'
    target = update.message.reply_to_message.from_user.username
    logger.info(msg=f"@{update.effective_user.username} did /butterfly to {target}")
    get(update, context, cmd)
    is_that_butterfly()
    update.message.reply_photo(open('output.jpg', 'rb'))
    os.remove('output.jpg')
    logger.info(msg=f"@{update.effective_user.username} /{cmd} SUCCESSFULL")


def bruh(update: Update, context: CallbackContext) -> None:
    cmd = 'bruh'
    target = update.message.reply_to_message.from_user.username
    logger.info(msg=f"@{update.effective_user.username} did /bruh to {target}")
    get(update, context, cmd)
    angry_pakistan_fan()
    update.message.reply_photo(open('output.jpg', 'rb'))
    os.remove('output.jpg')
    logger.info(msg=f"@{update.effective_user.username} /{cmd} SUCCESSFULL")


def strong(update: Update, context: CallbackContext) -> None:
    cmd = 'strong'
    target = update.message.reply_to_message.from_user.username
    logger.info(msg=f"@{update.effective_user.username} did /strong to {target}")
    get(update, context, cmd)
    strong_doge_weak_doge()
    update.message.reply_photo(open('output.jpg', 'rb'))
    os.remove('output.jpg')
    logger.info(msg=f"@{update.effective_user.username} /{cmd} SUCCESSFULL")


def weak(update: Update, context: CallbackContext) -> None:
    cmd = 'weak'
    target = update.message.reply_to_message.from_user.username
    logger.info(msg=f"@{update.effective_user.username} did /weak to {target}")
    get(update, context, cmd)
    weak_doge()
    update.message.reply_photo(open('output.jpg', 'rb'))
    os.remove('output.jpg')
    logger.info(msg=f"@{update.effective_user.username} /{cmd} SUCCESSFULL")


def fact(update: Update, context: CallbackContext) -> None:
    cmd = 'fact'
    target = update.message.reply_to_message.from_user.username
    logger.info(msg=f"@{update.effective_user.username} did /fact to {target}")
    get(update, context, cmd)
    facts_book()
    update.message.reply_photo(open('output.jpg', 'rb'))
    os.remove('output.jpg')
    logger.info(msg=f"@{update.effective_user.username} /{cmd} SUCCESSFULL")


def aa(update: Update, context: CallbackContext) -> None:
    cmd = 'aa'
    cxt = " ".join(context.args)
    htv_aliens_guy(cxt)
    update.message.reply_photo(open('output.png', 'rb'), quote=False)
    os.remove('output.png')
    logger.info(msg=f"@{update.effective_user.username} did /{cmd} {cxt}")
