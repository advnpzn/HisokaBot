from HisokaBot.helpers.constants import searchAnime
import nekos
from telegram import Update, InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardMarkup, \
    InlineKeyboardButton, ParseMode, InlineQueryResultPhoto
from telegram.ext import InlineQueryHandler, CallbackContext
from HisokaBot.helpers.anime_manga_htm_2_mdv2 import anime_manga_html_2_mdv2
from telegram.constants import MAX_MESSAGE_LENGTH
from uuid import uuid4
from HisokaBot.funcs.anime import search_anime_manga, s_chars
from HisokaBot.helpers.constants import ANIME_STR, searchChars


def inline_search(update: Update, context: CallbackContext):
    query = update.inline_query.query
    to_search = ['Anime', 'Manga', 'Character', 'Owo', 'Neko', 'Cheemsify', 'tc']
    if to_search[2] in query:
        inline_search_character(update, context)
    elif to_search[1] in query:
        inline_search_anime_manga(update, context, to_search[1])
    elif to_search[0] in query:
        inline_search_anime_manga(update, context, to_search[0])
    elif to_search[3] in query:
        inline_search_owoify(update, context)
    elif to_search[4] in query:
        inline_search_neko(update, context)
    elif to_search[5] in query:
        inline_search_cheemsify(update, context)
    elif to_search[6] in query:
        inline_search_tc(update, context)
    else:
        res = []
        for i in range(0, len(to_search)):
            res.append(
                InlineQueryResultArticle(id=uuid4(), title=to_search[i],
                                         input_message_content=InputTextMessageContent(message_text=
                                                                                       'Click the Button below'),
                                         reply_markup=InlineKeyboardMarkup(
                                             [
                                                 [InlineKeyboardButton(f"Search {to_search[i]}",
                                                                       switch_inline_query_current_chat=
                                                                       to_search[i]+" ")]
                                             ]
                                         ))
            )
        update.inline_query.answer(results=res)


def inline_search_character(update: Update, context: CallbackContext):
    query = update.inline_query.query
    s = s_chars(query.replace('Character', ''), 15)
    res = []
    for i in range(0, len(s)):
        name = s[i]['name']['full']
        image = s[i]['image']['large']
        desc = s[i]['description']
        try:
            if len(desc) > MAX_MESSAGE_LENGTH:
                desc = desc[:4092] + "..."
        except TypeError:
            pass
        res.append(
            InlineQueryResultArticle(
                 id=uuid4(),
                 title=name,
                 thumb_url=image,
                 hide_url=False,
                 input_message_content=InputTextMessageContent(message_text=f"*Name* : {name}\n"
                                                                            f"[‌]({image})\n"
                                                                            f"\n{desc}",
                                                               parse_mode=ParseMode.MARKDOWN,
                                                               disable_web_page_preview=False)
                 )
        )
    update.inline_query.answer(res)


def inline_search_anime_manga(update: Update, context: CallbackContext, stype: str):
    query = update.inline_query.query
    if stype == 'Manga':
        data = search_anime_manga(query.replace('Manga', ''), stype.upper(), 15)
        no_of_results = len(data)
        print(no_of_results)
        res = []
        for i in range(0, no_of_results):
            stats_img = f"https://img.anili.st/media/{data[i]['id']}"
            cover_img = data[i]['coverImage']['large']
            title_eng = data[i]['title']['english']
            title_rmj = data[i]['title']['romaji']
            title_nat = data[i]['title']['native']
            taipe = data[i]['type']
            genres = ', '.join(data[i]['genres'])
            status = data[i]['status']
            episodes = data[i]['episodes']
            mean_score = data[i]['meanScore']
            avg_score = data[i]['averageScore']
            duration = data[i]['duration']
            studios = ', '.join([data[i]['studios']['nodes'][j]['name'] for j in range(len(data[i]['studios']['nodes']))])
            premiered = f"{data[i]['startDate']['day']}-{data[i]['startDate']['month']}-{data[i]['startDate']['year']}"
            tags = ', '.join(data[i]['tags'][j]['name'] for j in range(len(data[i]['tags'])))
            description = data[i]['description']
            caption = ANIME_STR.format(
                title_eng,
                title_rmj,
                title_nat,
                stats_img,
                taipe,
                genres,
                status,
                episodes,
                mean_score,
                avg_score,
                duration,
                studios,
                premiered,
                tags,
                description
            )
            res.append(
                InlineQueryResultArticle(
                    id=uuid4(),
                    title=f"{title_rmj} | {title_nat}",
                    input_message_content=InputTextMessageContent(
                        message_text=anime_manga_html_2_mdv2(caption, data[i]['id']),
                        parse_mode=ParseMode.MARKDOWN_V2
                    ),
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [InlineKeyboardButton('More Information', url=data[i]['siteUrl'])]
                        ]
                    ),
                    thumb_url=cover_img,
                    description=f"{premiered} | {avg_score} | {status}"
                )
            )
        update.inline_query.answer(results=res)
    elif stype == 'Anime':
        data = search_anime_manga(query.replace('Anime', ''), stype.upper(), 15)
        no_of_results = len(data)
        print(no_of_results)
        res = []
        for i in range(0, no_of_results):
            stats_img = f"https://img.anili.st/media/{data[i]['id']}"
            cover_img = data[i]['coverImage']['large']
            title_eng = data[i]['title']['english']
            title_rmj = data[i]['title']['romaji']
            title_nat = data[i]['title']['native']
            taipe = data[i]['type']
            genres = ', '.join(data[i]['genres'])
            status = data[i]['status']
            episodes = data[i]['episodes']
            mean_score = data[i]['meanScore']
            avg_score = data[i]['averageScore']
            duration = data[i]['duration']
            studios = ', '.join(
                [data[i]['studios']['nodes'][j]['name'] for j in range(len(data[i]['studios']['nodes']))])
            premiered = f"{data[i]['startDate']['day']}-{data[i]['startDate']['month']}-{data[i]['startDate']['year']}"
            tags = ', '.join(data[i]['tags'][j]['name'] for j in range(len(data[i]['tags'])))
            description = data[i]['description']
            caption = ANIME_STR.format(
                title_eng,
                title_rmj,
                title_nat,
                stats_img,
                taipe,
                genres,
                status,
                episodes,
                mean_score,
                avg_score,
                duration,
                studios,
                premiered,
                tags,
                description
            )
            res.append(
                InlineQueryResultArticle(
                    id=uuid4(),
                    title=f"{title_rmj} | {title_nat}",
                    input_message_content=InputTextMessageContent(
                        message_text=anime_manga_html_2_mdv2(caption, data[i]['id']),
                        parse_mode=ParseMode.MARKDOWN_V2
                    ),
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [InlineKeyboardButton('More Information', url=data[i]['siteUrl'])]
                        ]
                    ),
                    thumb_url=cover_img,
                    description=f"{premiered} | {avg_score} | {status}"
                )
            )
        update.inline_query.answer(results=res)
        
        
 
def inline_search_tc(update: Update, context: CallbackContext):
    query = update.inline_query.query
    s = query.replace('tc', '')
    update.inline_query.answer(results=[
    InlineQueryResultArticle(
                 id=uuid4(),
                 title='Textcat',
                 input_message_content=InputTextMessageContent(message_text=nekos.textcat())
                 )])


def inline_search_neko(update: Update, context: CallbackContext):
    query = update.inline_query.query
    neko_url = nekos.cat()
    s = query.replace('tc', '')
    update.inline_query.answer(results=[
    InlineQueryResultPhoto(
        id=uuid4(),
        photo_url=neko_url,
        title='Neko',
        thumb_url=neko_url
    )])

def inline_search_owoify(update: Update, context: CallbackContext):
    query = update.inline_query.query
    s = query.replace('Owo', '')
    update.inline_query.answer(results=[
    InlineQueryResultArticle(
                 id=uuid4(),
                 title='Owo',
                 input_message_content=InputTextMessageContent(message_text=nekos.owoify(s))
                 )])


def inline_search_cheemsify(update: Update, context: CallbackContext):
    query = update.inline_query.query
    text = query.replace('Cheemsify', '').split(" ")
    holyWords = {
    'burger': 'burmger',
    'bad': 'bamd',
    'batman': 'bamtman',
    'cheese': 'cheems',
    'cheems': 'cheems',
    'cheeseburger': 'cheemsburger',
    'doge': 'domge',
    'female': 'f*male',
    'history': 'himstory',
    'nigger': 'n-word',
    'nigga': 'n-word',
    'retard': 'remtard',
    'woman': 'w*man',
    'women': 'w*men',
    'walter': 'walmter',
    'motherfucker': 'momtherfumcker',
    }

    for i in range(len(text)):
        if text[i] in holyWords.keys():
            text[i] = holyWords[text[i]]

    test = " ".join(text)
    cheemsed = test.replace('ck', 'mck').replace('ll', 'mll').replace('n', 'mn')
    update.inline_query.answer(results=[
    InlineQueryResultArticle(
                 id=uuid4(),
                 title='Cheemsify',
                 input_message_content=InputTextMessageContent(message_text=cheemsed)
                 )])
