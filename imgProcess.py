from PIL import Image, ImageDraw, ImageFont
import os

MEME_PATH = 'templates/'
FONT_PATH = 'fonts/'
PFP_PATH = 'pfp/'

fnt = ImageFont.truetype(FONT_PATH+'Menlo-Regular.ttf',size= 20)


def drake_meme():
    meme = Image.open(MEME_PATH+'drake.jpg')
    img1 = Image.open(PFP_PATH+'file_0.jpg')
    img2 = Image.open(PFP_PATH+'file_1.jpg')

    meme.paste(img2,(210,10))
    meme.paste(img1,(210,210))

    #draw = ImageDraw.Draw(meme)
    #draw.text((210,0),text=QUOTENAME,fill=(3, 132, 252),font=fnt)
    #draw.text((210,200),text=USERNAME,fill=(3, 132, 252),font=fnt)

    meme.save('output.jpg')
    os.remove(PFP_PATH+'file_0.jpg')
    os.remove(PFP_PATH+'file_1.jpg')

def batman_slap():
    meme = Image.open(MEME_PATH+'batman_slap.jpg')
    img1 = Image.open(PFP_PATH+'file_0.jpg').resize((100,100))
    img2 = Image.open(PFP_PATH+'file_1.jpg').resize((100,100))

    meme.paste(img2,(110,200))
    meme.paste(img1,(248,134))

    #draw = ImageDraw.Draw(meme)
    #draw.text((110,200),text=str(QUOTENAME),fill=(98, 3, 252),font=fnt)
    #draw.text((248,134),text=str(USERNAME),fill=(98, 3, 252),font=fnt)

    meme.save('output.jpg')
    os.remove(PFP_PATH+'file_0.jpg')
    os.remove(PFP_PATH+'file_1.jpg')

def ew_stepped_in_shit():
    meme = Image.open(MEME_PATH+'ew_stepped_in_shit.jpg')
    img1 = Image.open(PFP_PATH+'file_0.jpg').resize((51,44))
    img2 = Image.open(PFP_PATH+'file_1.jpg').resize((92,98))

    meme.paste(img2,(65,189))
    meme.paste(img1,(109,52))

    #draw = ImageDraw.Draw(meme)
    #draw.text((210,0),text=QUOTENAME,fill=(3, 132, 252),font=fnt)
    #draw.text((210,200),text=USERNAME,fill=(3, 132, 252),font=fnt)

    meme.save('output.jpg')
    os.remove(PFP_PATH+'file_0.jpg')
    os.remove(PFP_PATH+'file_1.jpg')

def is_that_butterfly():
    meme = Image.open(MEME_PATH+'is_that_butterfly.jpg')
    img1 = Image.open(PFP_PATH+'file_0.jpg').resize((170,179))
    img2 = Image.open(PFP_PATH+'file_1.jpg').resize((103,93))

    meme.paste(img2,(401,0))
    meme.paste(img1,(104,41))

    #draw = ImageDraw.Draw(meme)
    #draw.text((210,0),text=QUOTENAME,fill=(3, 132, 252),font=fnt)
    #draw.text((210,200),text=USERNAME,fill=(3, 132, 252),font=fnt)

    meme.save('output.jpg')
    os.remove(PFP_PATH+'file_0.jpg')
    os.remove(PFP_PATH+'file_1.jpg')

def woman_yelling_at_cat():
    meme = Image.open(MEME_PATH+'woman_yelling_at_cat.jpg')
    img1 = Image.open(PFP_PATH+'file_0.jpg').resize((115,96))
    img2 = Image.open(PFP_PATH+'file_1.jpg').resize((122,164))

    meme.paste(img2,(0,34))
    meme.paste(img1,(364,75))

    #draw = ImageDraw.Draw(meme)
    #draw.text((210,0),text=QUOTENAME,fill=(3, 132, 252),font=fnt)
    #draw.text((210,200),text=USERNAME,fill=(3, 132, 252),font=fnt)

    meme.save('output.jpg')
    os.remove(PFP_PATH+'file_0.jpg')
    os.remove(PFP_PATH+'file_1.jpg')

def is_for_me():
    meme = Image.open(MEME_PATH+'is_for_me.jpg')
    img1 = Image.open(PFP_PATH+'file_0.jpg').resize((177,161))
    

    meme.paste(img1,(129,79))

    #draw = ImageDraw.Draw(meme)
    #draw.text((210,0),text=QUOTENAME,fill=(3, 132, 252),font=fnt)
    #draw.text((210,200),text=USERNAME,fill=(3, 132, 252),font=fnt)

    meme.save('output.jpg')
    os.remove(PFP_PATH+'file_0.jpg')
    os.remove(PFP_PATH+'file_1.jpg')