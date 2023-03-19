from aiogram import Bot, Dispatcher, executor, types
import config
#from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

#05 отправка стикеров
#06 ---
#08 Клавиатура для бота
#10 inline keyboard 5:55
#11 Практика
#12 9:00 CallBack
#13
#16

bot_login = config.bot_login
TOKEN_API = config.api_reg #config.api_key

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

# kb = ReplyKeyboardMarkup(resize_keyboard=True) #!
# kb.add(KeyboardButton('/help'))

ikb = InlineKeyboardMarkup(row_width=2)
ib1 = InlineKeyboardButton(text='Btn1',
                           url='https://www.avito.ru/')
ib2 = InlineKeyboardButton(text='Btn2',
                           url='https://www.ya.ru/')

ikb.add(ib1, ib2)

HELP_COMMAND ='''
<b>/help</b> - <em>список команд</em>
<b>/start</b> - <em>start</em>
<b>/deskription</b> - <em>описание</em>
<b>/photo</b> - <em>фото</em>
'''

async def on_startup(_):
    print("Бот запущен")


@dp.message_handler(commands=['start'])
async def send_kb(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Hello!',
                           reply_markup=ikb)
    await message.delete()


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)

# @dp.message_handler(commands=['help'])
# async def help_command(message: types.Message):
#     await bot.send_message(chat_id=message.from_user.id,
#                            text=HELP_COMMAND,
#                            parse_mode='HTML',
#                            reply_markup=ReplyKeyboardRemove())
#     await message.delete()
#
# @dp.message_handler(commands=['deskription'])
# async def desc_command(message: types.Message):
#     await bot.send_message(chat_id=message.from_user.id,
#                            text='Бот пока нихера не умеет',
#                            parse_mode='HTML')
#     await message.delete()
#
# @dp.message_handler(commands=['photo'])
# async def photo_command(message: types.Message):
#     await bot.send_photo(chat_id=message.from_user.id,
#                          photo='https://62.img.avito.st/image/1/1.I8kftLa5jyApHU0lVYQBudcXiSqrl4firheNJKMdhSI.zfTIhZROAHFZ8O3988ql3HjBcSNLjAIYUWVtB18fmrw')
#     await message.delete()
#
# @dp.message_handler(commands=['give'])
# async def start_command(message: types.Message):
#     await bot.send_sticker(message.from_user.id, sticker='CAACAgIAAxkBAAEIAAHyZAQ4hwG9vLWqy19qxpzcbWMYVr4AAg4AA-nYEygTpj1DX_hIHy4E')
#     await message.delete()

