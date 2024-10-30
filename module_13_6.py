from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import asyncio

api = "Your token"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb1 = ReplyKeyboardMarkup(resize_keyboard=True)
button1 = KeyboardButton(text='Рассчитать')
button2 = KeyboardButton(text='Информация')
kb1.add(button1, button2)

kb_in = InlineKeyboardMarkup(resize_keyboard=True)
button_in_1 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button_in_2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
kb_in.add(button_in_1, button_in_2)


@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    await message.answer(text='Привет! Я бот помогающий твоему здоровью.', reply_markup=kb1)
    # await message.answer("'Для начала расчета введите слово 'Рассчитать'")


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(text=['Рассчитать'])
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=kb_in)


@dp.callback_query_handler(text=['formulas'])
async def get_formulas(call):
    str1 = 'для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5;'
    str2 = 'для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161.'
    await call.message.answer(f"{str1} \n {str2}")
    await call.answer()


@dp.callback_query_handler(text=['calories'])
async def set_age(call):
    await call.message.answer("Введите свой возраст:")
    await call.answer()
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer("Введите свой рост")
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    for_man = (10 * float(data['weight']) + 6.25 * float(data['growth']) -
               5 * float(data['age']) - 5)
    for_woman = for_man - 166
    await message.answer(f'Норма калорий для мужчин: {for_man}, для женщин: {for_woman}')
    await state.finish()


@dp.message_handler()
async def all_message(message):
    await message.answer("Введите команду /start, чтобы начать общение.")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)