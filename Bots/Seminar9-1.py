from aiogram import Bot, Dispatcher
from aiogram.utils import executor
from aiogram.types import Message

bot_gb = Bot("TOKEN")
dp = Dispatcher(bot_gb)


async def on_start(_):
    print('Бот запущен')

executor.start_polling(dp, skip_updates=True, on_startup=on_start)

@dp.message_handler(commands=['start'])
async def com_start(message: Message):
    await message.reply('Бот запущен и готов к работе')



@dp.message_handler()
async def com_start(message: Message):
    if message.text =='молодец':
        await message.reply(f'Спасибо, {message.from_user.first_name},'
                            f'ты тоже')
    elif message.text == 'дурак'