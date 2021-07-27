from aiogram import Bot, Dispatcher, types, executor

bot = Bot('1903081763:AAGgycCgHosNAdxJi2_Lo8Al9-6btq1g_l8', parse_mode='html')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer('Я работаю')

@dp.message_handler(content_types=['text'])
async def main(message: types.Message):
 if message.text.lower() == 'привет':
  await message.answer('Приветики')

if __name__ == '__main__':
    executor.start_polling(dp, fast=True, skip_updates=True)