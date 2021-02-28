import requests
from HisokaBot.helpers.constants import MEME_API_URI


def meme():
    r = requests.get(MEME_API_URI).json()
#    pprint(r)
    return {'title': r['title'], 'img_url': r['url'], 'post_url': r['postLink'], 'up_votes': r['ups'],
            'sub_reddit': f"r/{r['subreddit']}"}
