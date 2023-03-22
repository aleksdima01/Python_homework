from aiogram import Bot, Dispatcher
from aiogram.bot import bot
from aiogram.utils import executor
from aiogram.types import Message, ParseMode
import emoji
from aiogram.utils.markdown import bold, text

bot_gb = Bot("6236141184:AAHbG2qc87v8rX5cz0iUEPyaSjw2Kt_4GMs")
dp = Dispatcher(bot_gb)
img = open("Video.jpg", 'rb')

async def on_start(_):
    print('Бот запущен')



@dp.message_handler(commands=['start'])
async def com_start(message: Message):
    print(message)
    await message.reply('Бот запущен и готов к работе\nИспользуй /help, чтобы увидеть список доступных команд!')


@dp.message_handler(commands=['help'])
async def process_help_command(message: Message):
    msg = text(bold('Я могу ответить на следующие команды:'),
               '/photo''/exchange', sep='\n')
    await message.reply(msg, parse_mode=ParseMode.MARKDOWN)


@dp.message_handler(commands=['photo'])
async def process_photo_command(message: Message):
    caption = 'Я слежу за тобой! :eyes::video_camera:'
    await bot_gb.send_photo(message.from_user.id, img,
                          caption=emoji.emojize(caption),
                          reply_to_message_id=message.message_id)


@dp.message_handler()
async def com_start(message: Message):
    if message.text.lower() =='дима молодец':
        await message.reply(f'Спасибо, {message.from_user.first_name}, '
                            f'ты тоже')
    elif message.text.lower() == 'привет':
        await message.reply(f'Привет')
    elif message.text.lower() == 'дурак':
        await message.reply(f'Не ругайся, насяльника!')
    else:
        await message.reply(f'Не знаю такое, насяльника' + emoji.emojize(':upside-down_face:'))


executor.start_polling(dp, skip_updates=False, on_startup=on_start)