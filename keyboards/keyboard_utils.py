from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

# Инициализируем билдер
kb_builder = ReplyKeyboardBuilder()

# Создаем кнопки с добавлением смайликов
regular_btn = KeyboardButton(text='📋 Пройти опрос', callback_data='regular_quiz')
quiz_btn = KeyboardButton(text='🧠 Пройти викторину', callback_data='regular_quiz')

# Добавляем кнопки в билдер
kb_builder.row(regular_btn, quiz_btn, width=2)

# Создаем объект клавиатуры
keyboard: ReplyKeyboardMarkup = kb_builder.as_markup(
    resize_keyboard=True,
    one_time_keyboard=True
)
