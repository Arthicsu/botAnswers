from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from database.models import polls, quizzes
from keyboards.keyboard_utils import keyboard as default_keyboard
from StatesGroup.state import UserMode
from database.models import user_data

router = Router()

# Функция для отображения вопроса из опроса
async def ask_regular_question(message: Message):
    user_id = message.from_user.id
    step = user_data[user_id]["regular_step"]
    poll = polls[step]

    kb_builder = ReplyKeyboardBuilder()
    for option in poll["options"]:
        kb_builder.button(text=option)
    keyboard = kb_builder.as_markup(resize_keyboard=True)

    await message.answer(poll["question"], reply_markup=keyboard)

@router.message(F.text == "📋 Пройти опрос")
async def start_regular(message: Message, state: FSMContext):
    await state.set_state(UserMode.poll)
    user_data[message.from_user.id] = {"regular_step": 0}
    await ask_regular_question(message)

@router.message(F.text.in_([option for poll in polls for option in poll["options"]]))
async def handle_regular_answer(message: Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state == UserMode.poll:
        user_id = message.from_user.id
        step = user_data[user_id]["regular_step"]
        user_data[user_id].setdefault("regular_answers", []).append(message.text)

        if step + 1 < len(polls):
            user_data[user_id]["regular_step"] += 1
            await ask_regular_question(message)
        else:
            await message.answer("Спасибо за участие в опросе!", reply_markup=default_keyboard)
            await state.set_state(UserMode.copy)

# --- Викторина ---
async def ask_quiz_question(message: Message):
    user_id = message.from_user.id
    step = user_data[user_id]["quiz_step"]
    quiz = quizzes[step]

    kb_builder = ReplyKeyboardBuilder()
    for option in quiz["options"]:
        kb_builder.button(text=option)
    keyboard = kb_builder.as_markup(resize_keyboard=True)

    await message.answer(quiz["question"], reply_markup=keyboard)

@router.message(F.text == "🧠 Пройти викторину")
async def start_quiz(message: Message, state: FSMContext):
    await state.set_state(UserMode.quiz)
    user_data[message.from_user.id] = {"quiz_step": 0, "correct_answers": 0}  # Инициализируем счётчик
    await ask_quiz_question(message)

@router.message(F.text.in_([option for quiz in quizzes for option in quiz["options"]]))
async def handle_quiz_answer(message: Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state == UserMode.quiz:
        user_id = message.from_user.id
        step = user_data[user_id]["quiz_step"]
        quiz = quizzes[step]
        correct_option = quiz["options"][quiz["correct_option_id"]]

        # Проверяем ответ и обновляем счётчик
        if message.text == correct_option:
            user_data[user_id]["correct_answers"] += 1
            await message.answer("Правильно :)")
        else:
            await message.answer(f"Неправильно :(\nПравильный ответ: {correct_option}")

        # Переходим к следующему вопросу или завершаем викторину
        if step + 1 < len(quizzes):
            user_data[user_id]["quiz_step"] += 1
            await ask_quiz_question(message)
        else:
            # Отправляем итоговый результат
            score = user_data[user_id]["correct_answers"]
            total_questions = len(quizzes)
            await message.answer(
                f"Викторина окончена! Вы правильно ответили на {score} из {total_questions} вопросов.",
                reply_markup=default_keyboard
            )
            await state.set_state(UserMode.copy)