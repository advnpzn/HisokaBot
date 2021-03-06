import os


MEME_API_URI = os.environ.get('meme_api_uri')
BOT_TOKEN = os.environ.get('bot_token')
ANILIST_GRAPHQL_URI = os.environ.get('anilist_uri')
DATABASE_URI = os.environ.get("database_uri")


searchChars = '''
query ($search: String, $page: Int, $perPage: Int) {
  Page(page: $page, perPage: $perPage){
    characters(search: $search) {
      name {
        full
      }
      image {
        large
      }
      favourites
      description
    }
  }
}'''

searchAnime = '''
query ($type: MediaType $search: String, $page: Int, $perPage: Int) {
  Page(page: $page, perPage: $perPage){
    media(search: $search, type: $type){
      title{
        romaji
        english
        native
      }
      id
      coverImage {
        large
      }
      type
      genres
      status
      episodes
      meanScore
      averageScore
      duration
      status
      siteUrl
      characters {
        nodes {
          name {
            full
          }
        }
      }
      trailer {
        site
      }
      tags {
        name
      }
      startDate {
        year
        month
        day
      }
      description
      studios{
        nodes{
          name
        }
      }
    }
  }
}
'''

ANIME_STR = "<b>{} \| {} \| {} </b>[‌]({})\n"\
            "• <b>Type :</b> <pre>{}</pre>\n"\
            "• <b>Genre :</b> <pre>{}</pre>\n"\
            "• <b>Status :</b> <pre>{}</pre>\n"\
            "• <b>No of episodes :</b> <pre>{}</pre>\n"\
            "• <b>Mean Score :</b> <pre>{}</pre>\n"\
            "• <b>Average Score :</b> <pre>{}</pre>\n"\
            "• <b>Duration :</b> <pre>{} min(s)</pre>\n"\
            "• <b>Studio(s) :</b> <pre>{}</pre>\n"\
            "• <b>Premiered :</b> <pre>{}</pre>\n"\
            "• <b>Tags :</b> <pre>{}</pre>\n\n"\
            "• <b>Synopsis :</b> \n<pre>{}</pre>\n"


help_for_specific_commands = {
    'meme': {'pic': 'https://telegra.ph/file/79a8ec0f894d1173bddf0.png',
             'text': '''
Do /meme and get memes from famous subreddits.
                        '''},
    'slap': {'pic': 'https://telegra.ph/file/23ea683bb64d8525e5c36.png',
             'text': '''
Reply to another user in a Group with /slap and get modified Batman slap's Robin picture with you and your target's profile picture.
                        '''},
    'bruh': {'pic': 'https://telegra.ph/file/c31101b4095c893142a96.png',
             'text': '''
Reply to a user with /bruh and get Angry Pakistani Fan picture with your
                        '''},
    'aa': {'pic': 'https://telegra.ph/file/e6051f33eb81b13d20510.png',
           'text': '''
Do /aa <text> and get ancient aliens guy meme with the text.
No need to reply to a User.
e.g /aa karens
                        '''},
    'strong': {'pic': 'https://telegra.ph/file/a419142f37e44165a3558.png',
               'text': '''
Reply to another user in a Group with /strong and get modified Strong/Weak Doge picture with you and your target's profile picture.
                        '''},
    'hinsult': {'pic': 'https://telegra.ph/file/0b764766c0f6a9d24b1f0.png',
                'text': '''
Reply to another user in a Group with /hinsult to insult that person.
Note : Has a 50% chance of hisoka turning against the one who invoked /hinsult.
                        '''},
    'forme': {'pic': 'https://telegra.ph/file/9fa14f71af404c17371c8.png',
              'text': '''
Reply to another user in a Group with /forme and get modified is for me with your profile picture.
                        '''},
    'shit': {'pic': 'https://telegra.ph/file/8d01d28472f10bab87e1e.png',
             'text': '''
Reply to another user in a Group with /shit and get modified stepped in shit picture with you and your target's profile picture.
                        '''},
    'cat': {'pic': 'https://telegra.ph/file/bc4cc0a233ff899452267.png',
            'text': '''
Reply to another user in a Group with /cat and get modified Woman yelling at cat picture with you and your target's profile picture.
                        '''},
    'butterfly': {'pic': 'https://telegra.ph/file/780356416308c659e8f3a.png',
                  'text': '''
Reply to another user in a Group with /butterfly and get modified Is that a Butterfly meme picture with you and your target's profile picture.
                        '''},
    'start': {'pic': 'https://telegra.ph/file/df4aeaba98b912e640990.png',
              'text': '''
Hello {} .
I'm Hisoka. I can do a lot of tricks and jokes.
But the most important thing of all...,
Bungee Gum possesses the properties of both rubber and gum.
Click the Help button to check out my tricks.
Any suggestions/Improvements ? Contact Developer.
                        '''},
    'weak': {'pic': 'https://telegra.ph/file/8052218e7ee1a18167110.png',
             'text': '''
Reply to another user in a Group with /weak and get modified weak doge with your profile picture.
                        '''},
    'fact': {'pic': 'https://telegra.ph/file/c2d98dd061384618e8b64.png',
             'text': '''
Reply to another user in a Group with /fact and get modified Ed fact picture with you and your target's profile picture.
                        '''},
    'drake': {'pic': 'https://telegra.ph/file/c1ae3fe66336b05bc1ffa.png',
              'text': '''
Reply to another user in a Group with /drake and get modified Drake meme picture with you and your target's profile picture.
                        '''},
    'search_anime': {'pic': 'https://telegra.ph/file/82ac54b6ef3677ba1a5fb.png',
                     'text': '''
Do /anime and reply to it with an Anime Name or you can do /anime (anime)
e.g. /anime Eromanga Sensei
                        '''},
    'search_manga': {'pic': 'https://telegra.ph/file/d6a1fff9b205cd86292e0.png',
                     'text': '''
Do /manga and reply to it with a manga Name or you can do /manga (manga)
e.g. /manga black clover
                        '''},
    'anime_manga_section': {'pic': 'https://telegra.ph/file/2f487c56d138ec4816003.png',
                            'text': '''
Welcome to Anime/Manga Help Section UwU !
Click the Buttons to see their functions nyaa~
                        '''},
    'help_section': {'pic': 'https://telegra.ph/file/1bce7d2f3655d4bbdaab4.png',
                     'text': '''
Click the Buttons. 
                        '''},
    'img_manipulation_section': {'pic': 'https://telegra.ph/file/2c5680e4f4907cd0afe2e.png',
                                 'text': '''
Welcome to Image Manipulation Section!
We can even make you beautiful like Palm.
(Palm is the girl in photo)
What are you waiting for then..
                        '''},
}

templates = {
    'drake': 'https://telegra.ph/file/a3c4063b97478d702fb9f.jpg',
    'slap': 'https://telegra.ph/file/43393d9fcf9ca911f157b.jpg',
    'bruh': 'https://telegra.ph/file/376baa4636d7411205848.jpg',
    'htv_guy': 'https://telegra.ph/file/3d911a923e496df9f22dc.jpg',
    'strong': 'https://telegra.ph/file/b0db6b97c4d2922e0317a.jpg',
    'weak': 'https://telegra.ph/file/9bf2877489d728c0c35e3.jpg',
    'fact': 'https://telegra.ph/file/fddcbb8ff22488fa0c297.jpg',
    'shit': 'https://telegra.ph/file/0ab5e3e9d0951b2dbb109.jpg',
    'butterfly': 'https://telegra.ph/file/eb22b3e275a8cd3728490.jpg',
    'forme': 'https://telegra.ph/file/60316c94f2f860aaa1615.jpg',
    'cat': 'https://telegra.ph/file/5ede2db12f17f6306d906.jpg',
}
