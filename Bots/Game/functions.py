import random
from create_bot import dp
from aiogram.types import Message, ParseMode, ReplyKeyboardMarkup
import emoji
import total_candys
from aiogram.utils.markdown import bold, text

diff = 1


@dp.message_handler(commands=['diff'])
async def intro_function(message: Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttons = ["высокая", "низкая"]
    keyboard.add(*buttons)
    await message.reply(("Меняем сложность"), reply_markup=keyboard)


@dp.message_handler(text=['высокая', 'низкая'])
async def get_text_messages(message: Message):
    global diff
    if message.text.lower() == 'высокая':
        await message.answer('Выбрана высокая сложность!')
        diff = 1
    if message.text.lower() == 'низкая':
        await message.answer('Выбрана низкая сложность!')
        diff = 2


@dp.message_handler(commands=['start', 'начать'])
async def com_start(message: Message):
    print(message)
    await message.reply(text=f'Привет, {message.from_user.first_name}' + emoji.emojize(':waving_hand:') + '\n'
                             f'Сегодня поиграем в интересную игру! Кто последний заберет со стола конфетки'
                             + emoji.emojize(':candy:') + ', тот и победил!\n'
                             f'Брать можно от 1 до 28 штук за ход!\n'
                             f'Жми /new_game, чтобы начать!\n'
                             f'Используй /help, чтобы увидеть список доступных команд!')


@dp.message_handler(commands=['help'])
async def process_help_command(message: Message):
    msg = text(bold('Команды:'),
               '/newgame - начало игры',
               '/help - список команд',
               '/set 300 - введи, чтобы поменять количество конфет на 300.',
               'Можешь поменять на другое число! Изначально конфет будет 150' + emoji.emojize(':candy:'),
               '/diff - поменять сложность',
               sep='\n')
    await message.reply(msg, parse_mode=ParseMode.MARKDOWN)


@dp.message_handler(commands=['set'])
async def set_count(message: Message):
    candys_count = int(message.text.split()[1])
    if candys_count < 1:
        await message.reply(f'Нельзя установить меньше 1 конфеты! Попробуй еще раз!')
        candys_count = 150
    print(candys_count)
    total_candys.user_total_candys[message.from_user.id] = candys_count
    print(total_candys.user_total_candys)
    await message.reply(f'Количество конфет поменяно на {candys_count}!')

@dp.message_handler(commands='newgame')
async def mes_new_game(message: Message):
    name = message.from_user.first_name
    for game in total_candys.games:
        if message.from_user.id == game:
            await message.answer(f'{name} ты уже есть в игре, можешь продолжать играть!')
            break
    else:
        if len(total_candys.user_total_candys) == 0:
            total_candys.user_total_candys[message.from_user.id] = 150
        total_candys.user_game_candys[message.from_user.id] = total_candys.user_total_candys[message.from_user.id]
        await message.answer(text=f'На столе {total_candys.user_game_candys.get(message.from_user.id)} конфет. Кидаем жребий, кто берет первым.')
        coin = random.randint(0, 1)
        total_candys.games[message.from_user.id] = total_candys.user_game_candys.get(message.from_user.id)
        if coin:
            await message.answer(text=f'{message.from_user.first_name}, поздравляю!\n'
                                      f'Выпал орёл! Ты ходишь первым! Бери от 1 до 28 конфет.')
        else:
            await message.answer(text=f'{message.from_user.first_name}, не расстраивайся!\n'
                                      f'Первый ход делает бот!')
            await bot_turn(message)


@dp.message_handler()
async def any_mess(message: Message):
    name = message.from_user.first_name
    print(emoji.demojize(message.text))
    for game in total_candys.games:
        if message.from_user.id == game:
            if message.text.isdigit():
                if 0 < int(message.text) < 29:
                    await player_turn(message)
                    print(total_candys.games)
                    #print(total_candys.games[message.from_user.id])
                else:
                    await message.answer(text=f'Неправильно, {message.from_user.first_name}!\n'
                                              f'Конфет надо взять от 1 до 28! Попробуй еще раз!')
            else:
                await message.reply(f'Введи цифрами количество конфет:')
            break
    else:
        await message.reply(f'Не знаю такого, начинай новую игру /newgame' + emoji.emojize(':upside-down_face:'))


async def player_turn(message: Message):
    take_amount = int(message.text)
    total_candys.games[message.from_user.id] = total_candys.games.get(message.from_user.id) - take_amount
    name = message.from_user.first_name
    await message.answer(
        text=f'{name} взял {take_amount} конфет и на столе осталось {total_candys.games.get(message.from_user.id)}')
    if await check_for_victory(message, name):
        return
    await message.answer(text=f'Ходит бот!')
    await bot_turn(message)


async def bot_turn(message: Message):
    take_amount = 0
    current_total = total_candys.games.get(message.from_user.id)
    if current_total <= 28:
        take_amount = current_total
    else:
        if diff == 1:
            take_amount = current_total % 29 if current_total % 29 != 0 else 1
        else:
            take_amount = random.randint(1, 28)
    name = message.from_user.first_name
    total_candys.games[message.from_user.id] = total_candys.games.get(message.from_user.id) - take_amount
    await message.answer(
        text=f'Бот взял {take_amount} конфет и на столе осталось {total_candys.games.get(message.from_user.id)}')
    if await check_for_victory(message, 'Бот'):
        return
    await message.answer(text=f'{name}, твой ход!')


async def check_for_victory(message: Message, name: str):
    if total_candys.games.get(message.from_user.id) <= 0:
        await message.answer(text=f'Победил {name}! Хорошая игра! Играем снова? /newgame')
        total_candys.games.pop(message.from_user.id)
        return True
    return False