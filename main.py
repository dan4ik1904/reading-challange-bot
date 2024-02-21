from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

bot = Bot('6356508064:AAGJlsz8e2eZEDnmwDdjliTNPm6SLLTH4Pc')

dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markupInl = types.InlineKeyboardMarkup()
    markupInl.add(types.InlineKeyboardButton('Добавить книгу 📕', web_app=WebAppInfo(url='https://forms.gle/zEKpZismZvGM33vz6')))
    markupInl.add(types.InlineKeyboardButton('Результаты 📊',  web_app=WebAppInfo(url='https://docs.google.com/spreadsheets/d/19khBMTRnbUs8ua7AKGqT4BjCDBfZNu9JuOb9mUwh8aY/')))
    await message.answer(f'Добро пожаловать в клуб любителей книг📕❤️\n\nВместе мы хотим прочитать 330 книг в 2023/24 учебном году.', reply_markup=markupInl)



executor.start_polling(dp)