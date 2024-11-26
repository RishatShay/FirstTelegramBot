from aiogram import Bot, Dispatcher, types, executor
from Keyboards_for_Mein_TG_bot import TOKEN, COMMANDS_LIST, DESCRIPTION, EMOJIES, STICKERS, PHOTOS
from Keyboards_for_Mein_TG_bot import kb1, ikb1
from random import randint, choice

bot = Bot(TOKEN)
dp = Dispatcher(bot)


def start_up():
    print('Bot started successfully')


@dp.message_handler(commands=['start'])
async def start_bot(message: types.Message):
    await message.answer(text='Welcome to Bibi', reply_markup=kb1)
    await message.delete()


@dp.message_handler(commands=['help'])
async def give_help(message: types.Message):
    await message.answer(text=COMMANDS_LIST, parse_mode='HTML')
    await message.delete()


@dp.message_handler(commands=['description'])
async def give_description(message: types.Message):
    await message.answer(text=DESCRIPTION)
    await message.delete()


@dp.message_handler(commands=['random_animal'])
async def give_random_animal(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id, photo=choice(PHOTOS), reply_markup=ikb1)
    await message.delete()


@dp.message_handler(commands=['random_emoji'])
async def give_random_emoji(message: types.Message):
    await message.answer(text=choice(EMOJIES))
    await message.delete()


@dp.message_handler(commands=['random_sticker'])
async def give_random_sticker(message: types.Message):
    await bot.send_sticker(chat_id=message.chat.id, sticker=choice(STICKERS))
    await message.delete()


@dp.message_handler(commands=['random_location'])
async def give_random_location(message: types.Message):
    lati = randint(-90, 90)
    long = randint(-180, 180)
    await bot.send_location(chat_id=message.chat.id, latitude=lati, longitude=long)
    await message.delete()


@dp.message_handler()
async def just_text(message: types.Message):
    await message.reply(text='Sorry ChatGPT is not integrated into me yet. Please use command only from <b>/help</b>',
                        parse_mode='HTML')


@dp.callback_query_handler()
async def call_back_analyz(callback: types.CallbackQuery):
    if callback.data == 'like':
        await callback.answer('You voted this animal is cute')
    elif callback.data == 'dislike':
        await callback.answer('You voted this animal is creepy')
    else:
        await give_random_animal(callback.message)


executor.start_polling(dp, skip_updates=True, on_startup=start_up())
