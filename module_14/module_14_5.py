from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor
from crud_functions2 import initiate_db, get_all_products, add_user, is_included

API_TOKEN = ''

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = State()


keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
button_calculate = KeyboardButton('Рассчитать')
button_info = KeyboardButton('Информация')
button_buy = KeyboardButton('Купить')
button_register = KeyboardButton('Регистрация')
keyboard.add(button_calculate, button_info)
keyboard.add(button_buy, button_register)

inline_product_keyboard = InlineKeyboardMarkup(row_width=2)
button_product1 = InlineKeyboardButton('Белокочанная капуста', callback_data='product_buying')
button_product2 = InlineKeyboardButton('Баклажаны', callback_data='product_buying')
button_product3 = InlineKeyboardButton('Картофель', callback_data='product_buying')
button_product4 = InlineKeyboardButton('Сладкий перец', callback_data='product_buying')
inline_product_keyboard.add(button_product1, button_product2, button_product3, button_product4)

inline_keyboard = InlineKeyboardMarkup(row_width=2)
button_calories = InlineKeyboardButton('Рассчитать норму калорий', callback_data='calories')
button_formulas = InlineKeyboardButton('Формулы расчёта', callback_data='formulas')
inline_keyboard.add(button_calories, button_formulas)

confirm_keyboard = InlineKeyboardMarkup(row_width=2)
confirm_button_yes = InlineKeyboardButton('Да', callback_data='confirm_yes')
confirm_button_no = InlineKeyboardButton('Нет', callback_data='confirm_no')
confirm_keyboard.add(confirm_button_yes, confirm_button_no)


@dp.message_handler(Text(equals=['Рассчитать', 'Информация', 'Купить', 'Регистрация'], ignore_case=True),
                    state=RegistrationState.all_states)
async def confirm_cancellation(message: types.Message, state: FSMContext):
    await message.answer("Вы находитесь в процессе регистрации. Вы уверены, что хотите прервать его?",
                         reply_markup=confirm_keyboard)


@dp.callback_query_handler(Text(equals='confirm_yes'), state=RegistrationState.all_states)
async def cancel_registration(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer("Регистрация прервана. Все данные удалены.", reply_markup=keyboard)
    await state.finish()
    await call.answer()


@dp.callback_query_handler(Text(equals='confirm_no'), state=RegistrationState.all_states)
async def continue_registration(call: types.CallbackQuery):
    await call.message.answer("Продолжаем регистрацию. Введите необходимые данные.")
    await call.answer()


@dp.message_handler(commands=['start'], state=RegistrationState.all_states)
async def start_in_registration(message: types.Message, state: FSMContext):
    await message.answer("Вы находитесь в процессе регистрации. Вы уверены, что хотите прервать его?",
                         reply_markup=confirm_keyboard)


@dp.message_handler(commands=['start'], state=None)
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


@dp.message_handler(Text(equals='Регистрация', ignore_case=True))
async def sign_up(message: types.Message):
    await message.answer("Введите имя пользователя (только латинский алфавит):")
    await RegistrationState.username.set()


@dp.message_handler(state=RegistrationState.username)
async def set_username(message: types.Message, state: FSMContext):
    username = message.text

    if is_included(username):
        await message.answer("Пользователь существует, введите другое имя:")
        return

    await state.update_data(username=username)
    await message.answer("Введите свой email:")
    await RegistrationState.email.set()


@dp.message_handler(state=RegistrationState.email)
async def set_email(message: types.Message, state: FSMContext):
    email = message.text
    await state.update_data(email=email)
    await message.answer("Введите свой возраст:")
    await RegistrationState.age.set()


@dp.message_handler(state=RegistrationState.age)
async def set_age_registration(message: types.Message, state: FSMContext):
    try:
        age = int(message.text)
    except ValueError:
        await message.answer("Пожалуйста, введите корректное число для возраста.")
        return

    await state.update_data(age=age, balance=1000)

    data = await state.get_data()
    username = data.get('username')
    email = data.get('email')
    age = data.get('age')

    add_user(username=username, email=email, age=age)
    await message.answer(f"Вы успешно зарегистрировались! Ваше имя: {username}, возраст: {age}, email: {email}.")
    await message.answer("Что вы хотите сделать дальше?", reply_markup=keyboard)
    await state.finish()


@dp.message_handler(Text(equals='Купить', ignore_case=True))
async def get_buying_list(message: types.Message):
    products = get_all_products()

    for product in products:
        await message.answer(
            f"Название: {product[1]} | Описание: {product[2]} | Цена: {product[3]}"
        )
        with open(product[4], 'rb') as photo:
            await message.answer_photo(photo)

    await message.answer("Выберите продукт для покупки:", reply_markup=inline_product_keyboard)


@dp.callback_query_handler(Text(equals='product_buying'))
async def send_confirm_message(call: types.CallbackQuery):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()


@dp.message_handler()
async def all_messages(message: types.Message):
    await message.answer("Введите команду /start, чтобы начать общение.")


initiate_db()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
