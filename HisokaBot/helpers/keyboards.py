from telegram import InlineKeyboardButton, InlineKeyboardMarkup


back_to_imgmanipulation_help_button = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton('🔙', callback_data='back_to_imgmanipulation')],
        ])

back_to_anime_help_button = InlineKeyboardMarkup(
        [[InlineKeyboardButton('🔙', callback_data='back_to_anime')]])

help_funcs_buttons = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton('Image Manipulation', callback_data='h_imgmanipulation'), InlineKeyboardButton(
                'Anime', callback_data='h_anime')],
            [InlineKeyboardButton('🔙', callback_data='back_to_start')],

        ]
    )

anime_buttons = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton(
                    'Search Anime', callback_data='anime_animesearch')],
                [InlineKeyboardButton('🔙', callback_data='back_to_help')],
            ]
        )

img_manipulation_buttons = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton('Meme', callback_data='img_meme'), InlineKeyboardButton(
            'Bruh', callback_data='img_bruh'), InlineKeyboardButton('Slap', callback_data='img_slap'),
         InlineKeyboardButton('Drake', callback_data='img_drake')],
        [InlineKeyboardButton('HTV guy', callback_data='img_aa'), InlineKeyboardButton(
            'Strong', callback_data='img_strong'),
         InlineKeyboardButton('Hinsult', callback_data='img_hinsult'), ],
        [InlineKeyboardButton('Cat', callback_data='img_cat'), InlineKeyboardButton(
            'Is For Me', callback_data='img_forme'),
         InlineKeyboardButton('Shit', callback_data='img_shit'), ],
        [InlineKeyboardButton('Butterfly', callback_data='img_butterfly'), InlineKeyboardButton(
            'Weak', callback_data='img_weak'), InlineKeyboardButton('Fact', callback_data='img_fact'), ],
        [InlineKeyboardButton('🔙', callback_data='back_to_help')]
    ]
)


start_buttons = InlineKeyboardMarkup(
            [
                [InlineKeyboardButton('GitHub', url='https://github.com/adenosinetp10'), InlineKeyboardButton(
                    'Developer', url='https://t.me/ATPnull'), InlineKeyboardButton('Help', callback_data='help')]
            ]
        )