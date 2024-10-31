from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor

API_TOKEN = ''

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


# Основное меню с новой кнопкой "Купить"
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
button_calculate = KeyboardButton('Рассчитать')
button_info = KeyboardButton('Информация')
button_buy = KeyboardButton('Купить')  # Добавляем кнопку "Купить"
keyboard.add(button_calculate, button_info)
keyboard.add(button_buy)

# Inline клавиатура с продуктами
inline_product_keyboard = InlineKeyboardMarkup(row_width=2)
button_product1 = InlineKeyboardButton('Product1', callback_data='product_buying')
button_product2 = InlineKeyboardButton('Product2', callback_data='product_buying')
button_product3 = InlineKeyboardButton('Product3', callback_data='product_buying')
button_product4 = InlineKeyboardButton('Product4', callback_data='product_buying')
inline_product_keyboard.add(button_product1, button_product2, button_product3, button_product4)

# Клавиатура для расчёта калорий
inline_keyboard = InlineKeyboardMarkup(row_width=2)
button_calories = InlineKeyboardButton('Рассчитать норму калорий', callback_data='calories')
button_formulas = InlineKeyboardButton('Формулы расчёта', callback_data='formulas')
inline_keyboard.add(button_calories, button_formulas)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Привет! Я бот, помогающий твоему здоровью.", reply_markup=keyboard)


@dp.message_handler(Text(equals='Рассчитать', ignore_case=True))
async def main_menu(message: types.Message):
    await message.answer("Выберите опцию:", reply_markup=inline_keyboard)


@dp.callback_query_handler(Text(equals='formulas'))
async def get_formulas(call: types.CallbackQuery):
    formula = (
        "Формула Миффлина-Сан Жеора:\n"
        "10 * вес(кг) + 6.25 * рост(см) - 5 * возраст - 161"
    )
    await call.message.answer(formula)
    await call.answer()


@dp.callback_query_handler(Text(equals='calories'))
async def set_age(call: types.CallbackQuery):
    await call.message.answer("Введите свой возраст:")
    await UserState.age.set()
    await call.answer()


@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    try:
        age = int(message.text)
    except ValueError:
        await message.answer("Пожалуйста, введите корректное число для возраста.")
        return

    await state.update_data(age=age)
    await message.answer("Введите свой рост (в сантиметрах):")
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    try:
        growth = int(message.text)
    except ValueError:
        await message.answer("Пожалуйста, введите корректное число для роста.")
        return

    await state.update_data(growth=growth)
    await message.answer("Введите свой вес (в килограммах):")
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    try:
        weight = int(message.text)
    except ValueError:
        await message.answer("Пожалуйста, введите корректное число для веса.")
        return

    await state.update_data(weight=weight)

    data = await state.get_data()
    age = data.get('age')
    growth = data.get('growth')
    weight = data.get('weight')
    bmr = 10 * weight + 6.25 * growth - 5 * age + 5
    await message.answer(f"Ваша норма калорий: {bmr:.2f} ккал в день.")
    await message.answer("Что вы хотите сделать дальше?", reply_markup=keyboard)
    await state.finish()


# Обработка кнопки "Купить"
@dp.message_handler(Text(equals='Купить', ignore_case=True))
async def get_buying_list(message: types.Message):
    products = [
        {"name": "Product1", "description": "описание 1", "price": 100, "image": "for_14_3/1.jpg"},
        {"name": "Product2", "description": "описание 2", "price": 200, "image": "for_14_3/2.jpg"},
        {"name": "Product3", "description": "описание 3", "price": 300, "image": "for_14_3/3.jpg"},
        {"name": "Product4", "description": "описание 4", "price": 400, "image": "for_14_3/4.jpg"}
    ]

    for product in products:
        await message.answer(
            f"Название: {product['name']} | Описание: {product['description']} | Цена: {product['price']}"
        )
        with open(product['image'], 'rb') as photo:
            await message.answer_photo(photo)

    await message.answer("Выберите продукт для покупки:", reply_markup=inline_product_keyboard)


# Обработка выбора продукта
@dp.callback_query_handler(Text(equals='product_buying'))
async def send_confirm_message(call: types.CallbackQuery):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()


@dp.message_handler()
async def all_messages(message: types.Message):
    await message.answer("Введите команду /start, чтобы начать общение.")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
