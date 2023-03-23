from functions import dp
from aiogram.utils import executor


async def on_start(_):
    print('Бот запущен')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False, on_startup=on_start)
