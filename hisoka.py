from telegram import Update, ParseMode, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
import shutil
import random
import logging
import os
from config import BOT_TOKEN
from imgProcess import *
from telegram.ext import Updater, CommandHandler, CallbackContext, CallbackQueryHandler, Filters
from telegram.utils import helpers
from strings import help_for_specific_commands

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


class Start:
    def __init__(self, name):

        self.start_buttons = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton('GitHub', url='https://github.com/adenosinetp10'), InlineKeyboardButton(
                    'Developer', url='https://t.me/ATPnull'), InlineKeyboardButton('Help', callback_data='help')]
            ]
        )
        self.st_photo = help_for_specific_commands['start']['pic']
        self.st_text = help_for_specific_commands['start']['text'].format(name)


def start(update: Update, context: CallbackContext):
    st = Start(update.effective_user.first_name)
    update.message.reply_photo(
        photo=st.st_photo, caption=st.st_text, reply_markup=st.start_buttons)


def help_with_buttons(update: Update, context: CallbackContext):
    help_funcs_buttons = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton('Meme', callback_data='h_meme'), InlineKeyboardButton(
                'Bruh', callback_data='h_bruh'), InlineKeyboardButton('Slap', callback_data='h_slap'), InlineKeyboardButton('Drake', callback_data='h_drake')],
            [InlineKeyboardButton('HTV guy', callback_data='h_aa'), InlineKeyboardButton(
                'Strong', callback_data='h_strong'), InlineKeyboardButton('Hinsult', callback_data='h_hinsult'), ],
            [InlineKeyboardButton('Cat', callback_data='h_cat'), InlineKeyboardButton(
                'Is For Me', callback_data='h_forme'), InlineKeyboardButton('Shit', callback_data='h_shit'), ],
            [InlineKeyboardButton('Butterfly', callback_data='h_butterfly'), InlineKeyboardButton(
                'Weak', callback_data='h_weak'), InlineKeyboardButton('Fact', callback_data='h_fact'), ],
            [InlineKeyboardButton('🔙', callback_data='back_to_start')]
        ]
    )

    query = update.callback_query
    query.answer()
    query.message.edit_media(InputMediaPhoto(
        help_for_specific_commands['start']['pic'], "Click the Buttons to see the instrutions to use the Commands."), reply_markup=help_funcs_buttons)


def help_fucns(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    back_button = InlineKeyboardMarkup(
        [[InlineKeyboardButton('🔙', callback_data='back_to_help')]])
    match = query.data.split('_')[1]
    if match == 'meme':
        query.message.edit_media(InputMediaPhoto(
            help_for_specific_commands['meme']['pic'], help_for_specific_commands['meme']['text']), reply_markup=back_button)
    elif match == 'slap':
        query.message.edit_media(InputMediaPhoto(
            help_for_specific_commands['slap']['pic'], help_for_specific_commands['slap']['text']), reply_markup=back_button)
    elif match == 'shit':
        query.message.edit_media(InputMediaPhoto(
            help_for_specific_commands['shit']['pic'], help_for_specific_commands['shit']['text']), reply_markup=back_button)
    elif match == 'forme':
        query.message.edit_media(InputMediaPhoto(
            help_for_specific_commands['forme']['pic'], help_for_specific_commands['forme']['text']), reply_markup=back_button)
    elif match == 'butterfly':
        query.message.edit_media(InputMediaPhoto(
            help_for_specific_commands['butterfly']['pic'], help_for_specific_commands['butterfly']['text']), reply_markup=back_button)
    elif match == 'cat':
        query.message.edit_media(InputMediaPhoto(
            help_for_specific_commands['cat']['pic'], help_for_specific_commands['cat']['text']), reply_markup=back_button)
    elif match == 'fact':
        query.message.edit_media(InputMediaPhoto(
            help_for_specific_commands['fact']['pic'], help_for_specific_commands['fact']['text']), reply_markup=back_button)
    elif match == 'weak':
        query.message.edit_media(InputMediaPhoto(
            help_for_specific_commands['weak']['pic'], help_for_specific_commands['weak']['text']), reply_markup=back_button)
    elif match == 'strong':
        query.message.edit_media(InputMediaPhoto(
            help_for_specific_commands['strong']['pic'], help_for_specific_commands['strong']['text']), reply_markup=back_button)
    elif match == 'bruh':
        query.message.edit_media(InputMediaPhoto(
            help_for_specific_commands['bruh']['pic'], help_for_specific_commands['bruh']['text']), reply_markup=back_button)
    elif match == 'hinsult':
        query.message.edit_media(InputMediaPhoto(
            help_for_specific_commands['hinsult']['pic'], help_for_specific_commands['hinsult']['text']), reply_markup=back_button)
    elif match == 'aa':
        query.message.edit_media(InputMediaPhoto(
            help_for_specific_commands['aa']['pic'], help_for_specific_commands['aa']['text']), reply_markup=back_button)
    elif match == 'drake':
        query.message.edit_media(InputMediaPhoto(
            help_for_specific_commands['drake']['pic'], help_for_specific_commands['drake']['text']), reply_markup=back_button)


def back_button_handling(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    match = query.data.split('_')
    if match[2] == 'help':
        help_with_buttons(update, context)
    else:
        st = Start(update.effective_user.first_name)
        query.message.edit_caption(
            caption=st.st_text, reply_markup=st.start_buttons)


if __name__ == "__main__":

    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CallbackQueryHandler(help_fucns, pattern=r'h_'))
    dp.add_handler(CallbackQueryHandler(help_with_buttons, pattern='help'))
    dp.add_handler(CallbackQueryHandler(
        back_button_handling, pattern=r'back_to'))
    dp.add_handler(CommandHandler(
        'start', start, filters=Filters.chat_type.private, run_async=True))
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
    dp.add_handler(CommandHandler('hinsult', insult, run_async=True))
    dp.add_handler(CommandHandler('aa', aa, run_async=True))
    updater.start_polling()
    updater.idle()
