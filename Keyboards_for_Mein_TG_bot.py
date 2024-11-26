from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


TOKEN = '6211270663:AAFhDXq43F-saaQetL2BCqKa9scLIiIO544'  #telegram API token

# string with all emojies to take random (10)
EMOJIES = '❤️👍👎💋😀😍🤣😅😎🥳'

# stickers to take random one (10)
STICKERS = ('CAACAgIAAxkBAAEKCptk3LBveOocraCeHZXtB7BHpDMM6QAC6hMAAqqPoUuJgRRhGQ8OJTAE',
            'CAACAgIAAxkBAAEKCp1k3LB2iMFqeTzgvZ7AJLXZEuMCiwAChxUAAiMAAaBLV73BzYKM-wIwBA',
            'CAACAgIAAxkBAAEKCp9k3LB4VpmaQgm7lRduEoY7vEatSgAC6xYAAkcZqEtNlxX393snETAE',
            'CAACAgIAAxkBAAEKCqFk3LB6eD0NRsvEEudus-lzDkq76QACKhcAAktUoEuC6yy0FAABmRkwBA',
            'CAACAgIAAxkBAAEKCqNk3LB8Niefvh5MD5roECk81AZT5QACNhYAAnJroEul2k1dhz9kKTAE',
            'CAACAgIAAxkBAAEKCqVk3LB--SjlXxggmDv8BLJ9g4h7xwACKBYAArAOoUuS9aoVZQ9R8TAE',
            'CAACAgIAAxkBAAEKCqdk3LCAqe5ETPgHccoge6ZUCPI25QACTxYAAuZtoUuZtfczSttX5TAE',
            'CAACAgIAAxkBAAEKCqlk3LCCmnJKMf74zLiMWZ4a3W3bcgAClh0AApjaoUutLAfcw1JZrTAE',
            'CAACAgIAAxkBAAEKCqtk3LCE0h4U7ao2KcAYeOM9QSYJTgACBRoAAq6xsUvMplbk_0fTZjAE',
            'CAACAgIAAxkBAAEKCq1k3LCGzhWPXEh7dfkIDf_YrNPR2wAC6BUAAiMlyUtQqGgG1fAXAAEwBA')

# couple off all animals to take random (10)
PHOTOS =  ( # cute
           'https://cs9.pikabu.ru/post_img/2018/02/18/1/og_og_1518905506229333660.jpg',
           'https://i.pinimg.com/originals/13/e1/5c/13e15c8c03be62620aba74113261efee.jpg',
           'https://www.recreoviral.com/wp-content/uploads/2015/12/Fotograf%C3%ADas-m%C3%A1s-divertidas-de-animales-2015-10.jpg',
           'https://i.pinimg.com/originals/8a/78/47/8a784759f5c93fa8b7bb11b204e285a7.jpg',
           'https://getwallpapers.com/wallpaper/full/7/a/a/1483026-cool-baby-animal-background-wallpaper-1920x1440.jpg',
            # creepy
           'https://i.pinimg.com/originals/02/ac/79/02ac794f0a775011717ef2e03429cef2.jpg',
           'https://avatars.dzeninfra.ru/get-zen_doc/1872852/pub_5ccfecf4d31aa100b3452e11_5cd87edc6a662500ae49d182/scale_1200',
           'https://www.domesticatedcompanion.com/wp-content/uploads/cmg_images/141573/rid_3c666a42f61f284b221e8af6bbf63c52/24-72.jpg.pro-cmg.jpg',
           'https://funart.pro/uploads/posts/2021-04/1618100090_21-p-birmanskaya-kurnosaya-obezyana-zhivotnie-k-23.jpg',
           'https://forums.frontier.co.uk/attachments/5d1303e4-d464-4b56-b638-75845061d939-jpeg.149598/'
)

# all commands
COMMANDS_LIST = '''
<b>/start</b> - <i>start bot with standart parameters</i>
<b>/description</b> - <i>know more about my bot</i>
<b>/random_animal</b> - <i>you will see photo with an animal</i>
<b>/random_location</b> - <i>you can take a random point of Earth</i>
<b>/random_emoji</b> - <i>shows you a random emmoji</i>
<b>/random_sticker</b> - <i>show you a random sticker</i>
'''

# decription -------------------------------------------------------------------------------------------------!
DESCRIPTION = '''
I`m a bot. My name is Bibi, yea, like a robot from famous cartoon.
I was created by Rishat like a small project. Yet I can only send you random things like photos, emojies, stickers.
More over I can send you random location, I think it`s interesting to try to find accidentally your city or country.
I will learn more, but only if Rishat would teach me. I hope you you won`t be bored with me.
'''


kb1 = ReplyKeyboardMarkup(row_width=10)
# main interface Keyboard
b1 = KeyboardButton(text='/help')
b2 = KeyboardButton(text='/random_animal')
b3 = KeyboardButton(text='/random_location')
b4= KeyboardButton(text='/random_emoji')
b5= KeyboardButton(text='/random_sticker')
kb1.add(b1).add(b2).insert(b3).add(b4).insert(b5)


ikb1 = InlineKeyboardMarkup(row_width=100)
ib1 = InlineKeyboardButton(text='➡️➡️NEXT➡️➡️', callback_data='next')
ib2 = InlineKeyboardButton(text='👍LIKE👍', callback_data='like')
ib3 = InlineKeyboardButton(text='👎DISLIKE👎', callback_data='dislike')
ikb1.add(ib1).add(ib2).insert(ib3)
