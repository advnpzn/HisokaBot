import requests
from HisokaBot.helpers.constants import ANILIST_GRAPHQL_URI, searchAnime, ANIME_STR, searchChars
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, ParseMode
from telegram.ext import CallbackQueryHandler, CallbackContext
from HisokaBot.helpers.anime_manga_html_2_mdv2 import anime_manga_html_2_mdv2
from HisokaBot import dp

user_anime_dict = {}
user_manga_dict = {}


def search_anime_manga(name: str, stype: str,perPage: int):
    name = {
        'search': name,
        'page': 1,
        'perPage': perPage,
        'type': stype
    }
    r = requests.post(ANILIST_GRAPHQL_URI, json={'query': searchAnime, 'variables': name}).json()
    return r['data']['Page']['media']


def s_chars(name: str, perPage: int):
    var = {
        "search": f"{name}",
        "page": 1,
        "perPage": perPage
    }
    r = requests.post(url='https://graphql.anilist.co', json={'query': searchChars, 'variables': var}).json()
    return r['data']['Page']['characters']


def anime_manga(update: Update, context: CallbackContext, name, stype):
    data = search_anime_manga(name, stype, 6)
    user = update.effective_user
    if stype == 'ANIME':
        user_anime_dict[user.id] = data
    elif stype == 'MANGA':
        user_manga_dict[user.id] = data
    no_of_buttons = len(data)
    btn_list = []
    for i in range(no_of_buttons):
        btn_list.append(
            [
                InlineKeyboardButton(
                    text=data[i]['title']['english'] if data[i]['title']['english'] else data[i]['title']['romaji'],
                    callback_data=f"animesearch_{i}_{user.id}_{stype}")
            ]
        )
    update.message.reply_text(text="Your Search Result(s) :", reply_markup=InlineKeyboardMarkup(btn_list))


def anime_manga_when_clicked(update: Update, context: CallbackContext):
    query = update.callback_query
    match = query.data.split('_')  # match[0] = anime, match[1] = s_no., match[2] = user_id
    s_no = int(match[1])
    user_id = int(match[2])
    s_type = match[3]
    user = update.effective_user
    if user.id != user_id:
        query.answer(text="Not allowed!", show_alert=True)
        return -1
    query.answer("Wait..")
    query.message.delete()
    if s_type == 'ANIME':
        data = user_anime_dict[user_id][s_no]
    elif s_type == 'MANGA':
        data = user_manga_dict[user_id][s_no]
    caption = ANIME_STR.format(
        data['title']['english'],
        data['title']['romaji'],
        data['title']['native'],
        f"https://img.anili.st/media/{data['id']}",
        data['type'],
        ', '.join(data['genres']),
        data['status'],
        data['episodes'],
        data['meanScore'],
        data['averageScore'],
        data['duration'],
        ', '.join([data['studios']['nodes'][i]['name'] for i in range(len(data['studios']['nodes']))]),
        f"{data['startDate']['day']}-{data['startDate']['month']}-{data['startDate']['year']}",
        ', '.join(data['tags'][i]['name'] for i in range(len(data['tags']))),
        data['description'])
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=anime_manga_html_2_mdv2(caption, data['id']),
                             parse_mode=ParseMode.MARKDOWN_V2,
                             reply_markup=InlineKeyboardMarkup(
                                 [
                                     [InlineKeyboardButton('More Information', url=data['siteUrl'])],
                                 ]
                             ))


dp.add_handler(CallbackQueryHandler(anime_manga_when_clicked, pattern=r"animesearch_"))
