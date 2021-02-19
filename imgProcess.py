from PIL import Image, ImageDraw, ImageFont
import os
import requests
import json

MEME_PATH = 'templates/'
FONT_PATH = 'fonts/'
PFP_PATH = 'pfp/'
R_MEME_URL = os.environ.get("meme_api", "")

fnt = ImageFont.truetype(FONT_PATH+'Menlo-Regular.ttf', size=20)


def meme_generate():
    r = requests.get(R_MEME_URL).json()
    with open('m_img.png', 'wb') as f:
        f.write(requests.get(r['url']).content)
    return r['title']


def drake_meme():
    meme = Image.open(MEME_PATH+'drake.jpg')
    img1 = Image.open(PFP_PATH+'file_0.jpg')
    img2 = Image.open(PFP_PATH+'file_1.jpg')

    meme.paste(img2, (210, 10))
    meme.paste(img1, (210, 210))

    #draw = ImageDraw.Draw(meme)
    #draw.text((210,0),text=QUOTENAME,fill=(3, 132, 252),font=fnt)
    #draw.text((210,200),text=USERNAME,fill=(3, 132, 252),font=fnt)

    meme.save('output.jpg')
    os.remove(PFP_PATH+'file_0.jpg')
    os.remove(PFP_PATH+'file_1.jpg')


def batman_slap():
    meme = Image.open(MEME_PATH+'batman_slap.jpg')
    img1 = Image.open(PFP_PATH+'file_0.jpg').resize((100, 100))
    img2 = Image.open(PFP_PATH+'file_1.jpg').resize((100, 100))

    meme.paste(img2, (110, 200))
    meme.paste(img1, (248, 134))

    #draw = ImageDraw.Draw(meme)
    #draw.text((110,200),text=str(QUOTENAME),fill=(98, 3, 252),font=fnt)
    #draw.text((248,134),text=str(USERNAME),fill=(98, 3, 252),font=fnt)

    meme.save('output.jpg')
    os.remove(PFP_PATH+'file_0.jpg')
    os.remove(PFP_PATH+'file_1.jpg')


def ew_stepped_in_shit():
    meme = Image.open(MEME_PATH+'ew_stepped_in_shit.jpg')
    img1 = Image.open(PFP_PATH+'file_0.jpg').resize((51, 44))
    img2 = Image.open(PFP_PATH+'file_1.jpg').resize((92, 98))

    meme.paste(img2, (65, 189))
    meme.paste(img1, (109, 52))

    #draw = ImageDraw.Draw(meme)
    #draw.text((210,0),text=QUOTENAME,fill=(3, 132, 252),font=fnt)
    #draw.text((210,200),text=USERNAME,fill=(3, 132, 252),font=fnt)

    meme.save('output.jpg')
    os.remove(PFP_PATH+'file_0.jpg')
    os.remove(PFP_PATH+'file_1.jpg')


def is_that_butterfly():
    meme = Image.open(MEME_PATH+'is_that_butterfly.jpg')
    img1 = Image.open(PFP_PATH+'file_0.jpg').resize((170, 179))
    img2 = Image.open(PFP_PATH+'file_1.jpg').resize((103, 93))

    meme.paste(img2, (401, 0))
    meme.paste(img1, (104, 41))

    #draw = ImageDraw.Draw(meme)
    #draw.text((210,0),text=QUOTENAME,fill=(3, 132, 252),font=fnt)
    #draw.text((210,200),text=USERNAME,fill=(3, 132, 252),font=fnt)

    meme.save('output.jpg')
    os.remove(PFP_PATH+'file_0.jpg')
    os.remove(PFP_PATH+'file_1.jpg')


def woman_yelling_at_cat():
    meme = Image.open(MEME_PATH+'woman_yelling_at_cat.jpg')
    img1 = Image.open(PFP_PATH+'file_0.jpg').resize((115, 96))
    img2 = Image.open(PFP_PATH+'file_1.jpg').resize((122, 164))

    meme.paste(img2, (0, 34))
    meme.paste(img1, (364, 75))

    #draw = ImageDraw.Draw(meme)
    #draw.text((210,0),text=QUOTENAME,fill=(3, 132, 252),font=fnt)
    #draw.text((210,200),text=USERNAME,fill=(3, 132, 252),font=fnt)

    meme.save('output.jpg')
    os.remove(PFP_PATH+'file_0.jpg')
    os.remove(PFP_PATH+'file_1.jpg')


def is_for_me():
    meme = Image.open(MEME_PATH+'is_for_me.jpg')
    img1 = Image.open(PFP_PATH+'file_0.jpg').resize((177, 161))

    meme.paste(img1, (129, 79))

    #draw = ImageDraw.Draw(meme)
    #draw.text((210,0),text=QUOTENAME,fill=(3, 132, 252),font=fnt)
    #draw.text((210,200),text=USERNAME,fill=(3, 132, 252),font=fnt)

    meme.save('output.jpg')
    os.remove(PFP_PATH+'file_0.jpg')
    os.remove(PFP_PATH+'file_1.jpg')


def weak_doge():
    meme = Image.open(MEME_PATH+'weak_doge.jpg')
    img1 = Image.open(PFP_PATH+'file_0.jpg').resize((76, 66))
    #img2 = Image.open(PFP_PATH+'file_1.jpg').resize((92,98))

    # meme.paste(img2,(65,189))
    meme.paste(img1, (60, 33))

    #draw = ImageDraw.Draw(meme)
    #draw.text((210,0),text=QUOTENAME,fill=(3, 132, 252),font=fnt)
    #draw.text((210,200),text=USERNAME,fill=(3, 132, 252),font=fnt)

    meme.save('output.jpg')
    os.remove(PFP_PATH+'file_0.jpg')
    os.remove(PFP_PATH+'file_1.jpg')


def strong_doge_weak_doge():
    meme = Image.open(MEME_PATH+'strong_doge_weak_doge.jpg')
    img1 = Image.open(PFP_PATH+'file_0.jpg').resize((46, 44))
    img2 = Image.open(PFP_PATH+'file_1.jpg').resize((48, 41))

    meme.paste(img2, (295, 172))
    meme.paste(img1, (110, 79))

    #draw = ImageDraw.Draw(meme)
    #draw.text((210,0),text=QUOTENAME,fill=(3, 132, 252),font=fnt)
    #draw.text((210,200),text=USERNAME,fill=(3, 132, 252),font=fnt)

    meme.save('output.jpg')
    os.remove(PFP_PATH+'file_0.jpg')
    os.remove(PFP_PATH+'file_1.jpg')


def angry_pakistan_fan():
    meme = Image.open(MEME_PATH+'angry_pakistan_fan.jpg')
    img1 = Image.open(PFP_PATH+'file_0.jpg').resize((68, 85))
    #img2 = Image.open(PFP_PATH+'file_1.jpg').resize((48,41))

    # meme.paste(img2,(295,172))
    meme.paste(img1, (170, 16))

    #draw = ImageDraw.Draw(meme)
    #draw.text((210,0),text=QUOTENAME,fill=(3, 132, 252),font=fnt)
    #draw.text((210,200),text=USERNAME,fill=(3, 132, 252),font=fnt)

    meme.save('output.jpg')
    os.remove(PFP_PATH+'file_0.jpg')
    os.remove(PFP_PATH+'file_1.jpg')


def facts_book():
    meme = Image.open(MEME_PATH+'facts_book.jpg')
    img1 = Image.open(PFP_PATH+'file_0.jpg').resize((49, 48))
    img2 = Image.open(PFP_PATH+'file_1.jpg').resize((49, 48))
    meme.paste(img2, (17, 391))
    meme.paste(img1, (34, 319))

    #draw = ImageDraw.Draw(meme)
    #draw.text((210,0),text=QUOTENAME,fill=(3, 132, 252),font=fnt)
    #draw.text((210,200),text=USERNAME,fill=(3, 132, 252),font=fnt)

    meme.save('output.jpg')
    os.remove(PFP_PATH+'file_0.jpg')
    os.remove(PFP_PATH+'file_1.jpg')


def htv_aliens_guy(name):
    message = name.replace(' ', '\n')
    img = Image.open(MEME_PATH+'aa.jpg')
    draw = ImageDraw.Draw(img)
    bounding_box = [64, 183, 170, 215]
    x1, y1, x2, y2 = bounding_box
    w, h = draw.textsize(message, font=fnt)
    x = (x2 - x1 - w)/2 + x1
    y = (y2 - y1 - h)/2 + y1
    draw.text((x, y), message, align='center', font=fnt)
    img.save('output.png')
