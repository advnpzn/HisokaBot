from telegram import Update, ParseMode, InlineKeyboardButton, InlineKeyboardMarkup
import shutil
import os
import random
import logging
from imgProcess import *
from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram.utils import helpers

# Logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)


def meme(update: Update, context: CallbackContext) -> None:
    a = meme_generate()
    update.message.reply_photo(open('m_img.png', 'rb'), caption=a, quote=False)


def get(update, context):
    try:
        pfp = update.message.reply_to_message.from_user.get_profile_photos(
        ).photos[0][0].get_file().download()
        shutil.move(pfp, "pfp/file_1.jpg")
        pfp = update.message.from_user.get_profile_photos(
        ).photos[0][0].get_file().download()
        shutil.move(pfp, "pfp/file_0.jpg")
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


def help(update: Update, context: CallbackContext) -> None:
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton(
            "Help", callback_data="https://t.me/hisokaDankBot?start=help")]
    ])
    if update.effective_chat.GROUP:
        update.message.reply_text(
            "<pre>Click the Help Button.</pre>", parse_mode=ParseMode.HTML, reply_markup=keyboard)
    else:
        msg = ("<pre>/meme</pre> - Shows a random meme from Reddit\n"
               "<pre>/drake</pre> - Shows modified drake meme with user & target's Picture\n"
               "<pre>/slap</pre> - Shows modified Batman Slap meme with user & target's Picture\n"
               "<pre>/help</pre> - Shows available Commands.\n"
               "<pre>/hinsult</pre> - Insults the target, NOTE: Has a 50% \chance of insulting yourself!\n"
               "<pre>/weak</pre> - Shows modified Doge meme with user's Picture\n"
               "<pre>/strong</pre> - Shows modified Strong & Weak Doge meme with user & target's Picture\n"
               "<pre>/bruh</pre> - Shows modified Pakistani Fan meme with user's Picture\n"
               "<pre>/aa (text)</pre> - Shows modified Ancient aliens guy meme with user given text. e.g <pre>/aa indians</pre>")
        update.message.reply_text(msg, parse_mode=ParseMode.HTML)


def insult(update: Update, context: CallbackContext) -> None:
    print(update.message.from_user.username)
    try:
        if update.message.reply_to_message.from_user.username == 'hisokaDankBot':
            update.message.reply_text(
                "Did you know?\nBungee Gum possesses the properties of both rubber and gum.\nDon't try anything funny with me bro.")
        else:
            try:
                username_quote = '@'+update.message.reply_to_message.from_user.username
            except TypeError:
                username_quote = update.message.reply_to_message.from_user.first_name
            try:
                username_user = '@'+update.message.from_user.username
            except TypeError:
                username_user = update.message.from_user.first_name
            with open('insult.txt') as f:
                insult = random.choice(f.readlines())
                if "##name##" in insult:
                    insult = insult.replace("##name##", username_quote)
                    update.message.reply_text(insult, quote=False)
                else:
                    update.message.reply_text(f'{username_user} {insult}\n\nYou just got played yourself.\n'
                                              'Remember Bungee Gum?\nJust like that, this possesses both\n'
                                              'the properties of insulting and getting insulted.\nHave a Nice Day :)', quote=False)
    except AttributeError:
        update.message.reply_text('Reply to a User, Idiot!')


if __name__ == "__main__":

    bot_token = os.environ.get("BOT_TOKEN", "")
    updater = Updater(bot_token, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("drake", drake, run_async=True))
    dp.add_handler(CommandHandler("slap", slap, run_async=True))
    dp.add_handler(CommandHandler("shit", shit, run_async=True))
    dp.add_handler(CommandHandler("cat", cat, run_async=True))
    dp.add_handler(CommandHandler("forme", forme, run_async=True))
    dp.add_handler(CommandHandler("meme", meme, run_async=True))
    dp.add_handler(CommandHandler("butterfly", butterfly, run_async=True))
    dp.add_handler(CommandHandler("fact", fact, run_async=True))
    dp.add_handler(CommandHandler("weak", weak, run_async=True))
    dp.add_handler(CommandHandler("strong", strong, run_async=True))
    dp.add_handler(CommandHandler("bruh", bruh, run_async=True))
    dp.add_handler(CommandHandler("help", help, run_async=True))
    dp.add_handler(CommandHandler('hinsult', insult, run_async=True))
    dp.add_handler(CommandHandler('aa', aa, run_async=True))
    updater.start_polling()
    updater.idle()
