from telegram import Update, ParseMode, InlineKeyboardButton, InlineKeyboardMarkup
import shutil
import os
import random
import logging
from imgProcess import *
from telegram.ext import Updater, CommandHandler, CallbackContext, CallbackQueryHandler, Filters
from telegram.utils import helpers
import time

# Logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)

# CALL_BACK_DATA
KEYBOARD_HELP_CALLBACK_DATA = 'K-H-CB'
HELP = 'help'


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
    if update.effective_chat['type'] == 'group' or update.effective_chat['type'] == 'supergroup':
        msg = update.message.reply_text(
            "<pre>Click the Help Button.</pre>", parse_mode=ParseMode.HTML, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('Help', callback_data=KEYBOARD_HELP_CALLBACK_DATA)]]))
        context.job_queue.run_once(callback=delete_msg, when=5, context=[
                                   update.effective_chat.id, msg.message_id], name='del_help')
        update.message.delete()
    else:
        help_func(update, context)


def help_func(update: Update, context: CallbackContext) -> None:
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


def help_callback(update: Update, context: CallbackContext) -> None:
    url = helpers.create_deep_linked_url(context.bot.username, payload=HELP)
    update.callback_query.answer(url=url)


def delete_msg(context):

    job = context.job
    context.bot.delete_message(
        chat_id=job.context[0], message_id=job.context[1])


def start(update: Update, context: CallbackContext) -> None:
    keyboard = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton('Source Code', url='https://github.com/adenosinetp10/HisokaBot'), InlineKeyboardButton(
                'Developer', url='https://t.me/ATPnull'), InlineKeyboardButton('Help', callback_data=KEYBOARD_HELP_CALLBACK_DATA)]
        ]
    )
    msg = update.message.reply_text("<pre>Hey, I'm Hisoka.\n"
                                    "Did you know?\n"
                                    "Bungee Gum possesses the properties of both rubber and gum.\nWill be deleted in 5 secs to avoid flooding.</pre>", quote=False, parse_mode=ParseMode.HTML, reply_markup=keyboard)
    context.job_queue.run_once(callback=delete_msg, when=5, context=[
                               update.effective_chat.id, msg.message_id], name='del')
    update.message.delete()


if __name__ == "__main__":

    bot_token = os.environ.get("BOT_TOKEN", "")
    updater = Updater(bot_token, use_context=True)
    dp = updater.dispatcher
    job = updater.job_queue
    dp.add_handler(CallbackQueryHandler(
        help_callback, pattern=KEYBOARD_HELP_CALLBACK_DATA))
    dp.add_handler(CommandHandler("drake", drake, run_async=True))
    dp.add_handler(CommandHandler('start', help_func,
                                  Filters.regex(HELP), run_async=True))
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
    dp.add_handler(CommandHandler('start', start, run_async=True))
    updater.start_polling()
    updater.idle()
