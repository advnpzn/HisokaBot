from HisokaBot import dp
from telegram import InputMediaPhoto, Update
from telegram.ext import CallbackContext, CallbackQueryHandler
from HisokaBot.helpers.constants import help_for_specific_commands
from HisokaBot.helpers.keyboards import *


class ToStart:
    def __init__(self, name):

        self.to_start_buttons = start_buttons
        self.to_start_photo = help_for_specific_commands['start']['pic']
        self.to_start_text = help_for_specific_commands['start']['text'].format(name)


class ToHelp:
    def __init__(self):

        self.to_help_buttons = help_funcs_buttons
        self.to_help_photo = help_for_specific_commands['help_section']['pic']
        self.to_help_text = help_for_specific_commands['help_section']['text']


class ToAnime:
    def __init__(self):

        self.to_anime_buttons = anime_buttons
        self.to_anime_photo = help_for_specific_commands['anime_manga_section']['pic']
        self.to_anime_text = help_for_specific_commands['anime_manga_section']['text']


class ToImgmanipulation:
    def __init__(self):

        self.to_imgmanipulation_buttons = img_manipulation_buttons
        self.to_imgmanipulation_photo = help_for_specific_commands['img_manipulation_section']['pic']
        self.to_imgmanipulation_text = help_for_specific_commands['img_manipulation_section']['text']


def help_funcs(update: Update, context: CallbackContext):

    query = update.callback_query
    query.answer('Hold on..')
    query.message.edit_media(InputMediaPhoto(
        help_for_specific_commands['help_section']['pic'], help_for_specific_commands['help_section']['text']),
        reply_markup=help_funcs_buttons)


def help_funcs_handler(update: Update, context: CallbackContext):  #r="h_"
    query = update.callback_query
    query.answer(text='Hold on..', show_alert=False)
    match = query.data.split('_')[1]
    if match == 'am':    #h_am
        query.message.edit_media(InputMediaPhoto(help_for_specific_commands['anime_manga_section']['pic'],
                                                 help_for_specific_commands['anime_manga_section']['text']),
                                 reply_markup=anime_buttons)
    elif match == 'imgmanipulation':    #h_imgmanipulation
        query.message.edit_media(InputMediaPhoto(help_for_specific_commands['img_manipulation_section']['pic'],
                                                 help_for_specific_commands['img_manipulation_section']['text']),
                                 reply_markup=img_manipulation_buttons)


def help_img_manipulation_funcs_handler(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer(text='Hold on..', show_alert=False)
    match = query.data.split('_')[1]
    if match == 'meme':
        query.message.edit_media(InputMediaPhoto(
            help_for_specific_commands['meme']['pic'], help_for_specific_commands['meme']['text']),
            reply_markup=back_to_imgmanipulation_help_button)
    elif match == 'slap':
        query.message.edit_media(InputMediaPhoto(
            help_for_specific_commands['slap']['pic'], help_for_specific_commands['slap']['text']),
            reply_markup=back_to_imgmanipulation_help_button)
    elif match == 'shit':
        query.message.edit_media(InputMediaPhoto(
            help_for_specific_commands['shit']['pic'], help_for_specific_commands['shit']['text']),
            reply_markup=back_to_imgmanipulation_help_button)
    elif match == 'forme':
        query.message.edit_media(InputMediaPhoto(
            help_for_specific_commands['forme']['pic'], help_for_specific_commands['forme']['text']),
            reply_markup=back_to_imgmanipulation_help_button)
    elif match == 'butterfly':
        query.message.edit_media(InputMediaPhoto(
            help_for_specific_commands['butterfly']['pic'], help_for_specific_commands['butterfly']['text']),
            reply_markup=back_to_imgmanipulation_help_button)
    elif match == 'cat':
        query.message.edit_media(InputMediaPhoto(
            help_for_specific_commands['cat']['pic'], help_for_specific_commands['cat']['text']),
            reply_markup=back_to_imgmanipulation_help_button)
    elif match == 'fact':
        query.message.edit_media(InputMediaPhoto(
            help_for_specific_commands['fact']['pic'], help_for_specific_commands['fact']['text']),
            reply_markup=back_to_imgmanipulation_help_button)
    elif match == 'weak':
        query.message.edit_media(InputMediaPhoto(
            help_for_specific_commands['weak']['pic'], help_for_specific_commands['weak']['text']),
            reply_markup=back_to_imgmanipulation_help_button)
    elif match == 'strong':
        query.message.edit_media(InputMediaPhoto(
            help_for_specific_commands['strong']['pic'], help_for_specific_commands['strong']['text']),
            reply_markup=back_to_imgmanipulation_help_button)
    elif match == 'bruh':
        query.message.edit_media(InputMediaPhoto(
            help_for_specific_commands['bruh']['pic'], help_for_specific_commands['bruh']['text']),
            reply_markup=back_to_imgmanipulation_help_button)
    elif match == 'hinsult':
        query.message.edit_media(InputMediaPhoto(
            help_for_specific_commands['hinsult']['pic'], help_for_specific_commands['hinsult']['text']),
            reply_markup=back_to_imgmanipulation_help_button)
    elif match == 'aa':
        query.message.edit_media(InputMediaPhoto(
            help_for_specific_commands['aa']['pic'], help_for_specific_commands['aa']['text']),
            reply_markup=back_to_imgmanipulation_help_button)
    elif match == 'drake':
        query.message.edit_media(InputMediaPhoto(
            help_for_specific_commands['drake']['pic'], help_for_specific_commands['drake']['text']),
            reply_markup=back_to_imgmanipulation_help_button)


def help_anime_funcs_handler(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer(text='Hold on..', show_alert=False)
    match = query.data.split('_')[1]
    if match == 'animesearch':
        query.message.edit_media(InputMediaPhoto(
            help_for_specific_commands['search_anime']['pic'],
            caption=help_for_specific_commands['search_anime']['text']),
            reply_markup=back_to_anime_help_button)
    if match == 'mangasearch':
        query.message.edit_media(InputMediaPhoto(
            help_for_specific_commands['search_manga']['pic'],
            caption=help_for_specific_commands['search_manga']['text']),
            reply_markup=back_to_anime_help_button)


def back_button_handler(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    match = query.data.split('_')
    if match[2] == 'help':
        th = ToHelp()
        query.message.edit_media(InputMediaPhoto(th.to_help_photo, caption=th.to_help_text),
                                 reply_markup=th.to_help_buttons)
    elif match[2] == 'am':
        th = ToAnime()
        query.message.edit_media(InputMediaPhoto(th.to_anime_photo, caption=th.to_anime_text),
                                 reply_markup=th.to_anime_buttons)
    elif match[2] == 'imgmanipulation':
        th = ToImgmanipulation()
        query.message.edit_media(InputMediaPhoto(th.to_imgmanipulation_photo, caption=th.to_imgmanipulation_text),
                                 reply_markup=th.to_imgmanipulation_buttons)
    elif match[2] == 'start':
        st = ToStart(update.effective_user.first_name)
        query.message.edit_media(InputMediaPhoto(st.to_start_photo, caption=st.to_start_text),
                                 reply_markup=st.to_start_buttons)


dp.add_handler(CallbackQueryHandler(
        help_funcs_handler, pattern=r"h_"))
dp.add_handler(CallbackQueryHandler(
        help_img_manipulation_funcs_handler, pattern=r'img_'))
dp.add_handler(CallbackQueryHandler(
        help_anime_funcs_handler, pattern=r'am_'))
dp.add_handler(CallbackQueryHandler(
        help_funcs, pattern='help'))
dp.add_handler(CallbackQueryHandler(
        back_button_handler, pattern=r'back_to'))
