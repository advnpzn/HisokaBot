from telegram import Update, ParseMode, ForceReply
import shutil
import random
from HisokaBot import dp, updater
from HisokaBot.helpers.keyboards import *
from HisokaBot.funcs.meme import meme
from HisokaBot.funcs.anime import anime
from HisokaBot.funcs.imgProcess import *
from telegram.ext import CommandHandler, CallbackContext, Filters, ConversationHandler, MessageHandler
from HisokaBot.helpers.callbackquery_handlers import ToStart


def meme_generate(update: Update, context: CallbackContext) -> None:
    m = meme()
    url_post_btn = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton(text='Post Link', url=m['post_url'])]
        ]
    )
    update.message.reply_photo(photo=m['img_url'],
                               caption=f"<b>{m['title']}</b>\n"
                                       f"Subreddit: {m['sub_reddit']}\n"
                                       f"UpVotes ⬆️: {m['up_votes']}",
                               reply_markup=url_post_btn,
                               parse_mode=ParseMode.HTML)


def get(update, context):
    try:
        pfp = update.message.reply_to_message.from_user.get_profile_photos(
        ).photos[0][0].get_file().download()
        shutil.move(pfp, "HisokaBot/funcs/pfp/file_1.jpg")
        pfp = update.message.from_user.get_profile_photos(
        ).photos[0][0].get_file().download()
        shutil.move(pfp, "HisokaBot/funcs/pfp/file_0.jpg")
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
                "Did you know?\nBungee Gum possesses the properties of both rubber and gum.\n"
                "Don't try anything funny with me bro.")
        else:
            try:
                username_quote = '@'+update.message.reply_to_message.from_user.username
            except TypeError:
                username_quote = update.message.reply_to_message.from_user.first_name
            try:
                username_user = '@'+update.message.from_user.username
            except TypeError:
                username_user = update.message.from_user.first_name
            with open('HisokaBot/insult.txt') as f:
                insult = random.choice(f.readlines())
                if "##name##" in insult:
                    insult = insult.replace("##name##", username_quote)
                    update.message.reply_text(insult, quote=False)
                else:
                    update.message.reply_text(f'{username_user} {insult}\n\nYou just got played yourself.\n'
                                              'Remember Bungee Gum?\nJust like that, this possesses both\n'
                                              'the properties of insulting and getting insulted.\nHave a Nice Day :)',
                                              quote=False)
    except AttributeError:
        update.message.reply_text('Reply to a User, Idiot!')


def anime_cmd(update: Update, context: CallbackContext):
    query = ' '.join(context.args)
    if len(query) < 1:
        update.message.reply_text('Enter the Anime that you want to Search.',
                                  reply_markup=ForceReply(force_reply=True))
        return 69
    else:
        anime(update, context, query)


def anime_state(update: Update, context: CallbackContext):
    query = update.message.text
    anime(update, context, query)
    return 420


def cancel(update: Update, context: CallbackContext):
    context.bot.sendMessage("You cancelled.")
    return ConversationHandler.END


def start(update: Update, context: CallbackContext):
    if update.effective_chat['type'] == 'group' or update.effective_chat['type'] == 'supergroup':
        update.message.reply_text("Click the Button, I'll show you what I can do.", reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton('🃏', url='https://t.me/hisokaDankBot?start=true')]
            ]
        ))
    else:
        st = ToStart(update.effective_user.first_name)
        update.message.reply_photo(
            photo=st.to_start_photo, caption=st.to_start_text, reply_markup=st.to_start_buttons)


def main():
    dp.add_handler(ConversationHandler(entry_points=[CommandHandler('anime', anime_cmd, run_async=True)],
                                       states={
                                           69: [MessageHandler(Filters.text & ~ Filters.command, anime_state)]
                                       },
                                       fallbacks=[CommandHandler('cancel', cancel, run_async=True)],
                                       conversation_timeout=120,
                                       allow_reentry=True))
    dp.add_handler(CommandHandler("drake", drake, run_async=True))
    dp.add_handler(CommandHandler("slap", slap, run_async=True))
    dp.add_handler(CommandHandler("shit", shit, run_async=True))
    dp.add_handler(CommandHandler("cat", cat, run_async=True))
    dp.add_handler(CommandHandler("forme", forme, run_async=True))
    dp.add_handler(CommandHandler("meme", meme_generate, run_async=True))
    dp.add_handler(CommandHandler("butterfly", butterfly, run_async=True))
    dp.add_handler(CommandHandler("fact", fact, run_async=True))
    dp.add_handler(CommandHandler("weak", weak, run_async=True))
    dp.add_handler(CommandHandler("strong", strong, run_async=True))
    dp.add_handler(CommandHandler("bruh", bruh, run_async=True))
    dp.add_handler(CommandHandler('hinsult', insult, run_async=True))
    dp.add_handler(CommandHandler('aa', aa, run_async=True))
    dp.add_handler(CommandHandler(
        'start', start, run_async=True))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
