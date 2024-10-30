# Многофункциональный бот-пересыльщик с режимами опросов и викторин

Бот для Telegram, который может пересылать сообщения, а также предоставлять пользователям опросы и викторины. Основной режим работы бота — пересылка сообщений в режиме "copy". Однако, при вводе команды `/start` он переходит в режим выбора, где пользователи могут выбрать между прохождением опроса и викторины. <br />
Сделал студент ___группы ИВТ-201 Рощин Никита___

## Описание
Проект разработан на Python с использованием библиотеки __aiogram__, реализующей асинхронную работу с Telegram API. В боте предусмотрены следующие возможности:
- **Пересылка сообщений**: бот работает в режиме копирования всех сообщений по умолчанию.
- **Опросы**: бот задаёт серию вопросов и получает ответы с помощью кастомной клавиатуры.
- **Викторины**: бот предлагает вопросы с вариантами ответов и подсчитывает количество правильных ответов по окончании викторины.

## Установка
Прежде всего для корректной работы кода необходимо установить специальные библиотеки, которые описаны в файле ___"requirements.txt"___.
Соответственно:
1. Клонируйте репозиторий.
2. Устанавливаете все необходимые библиотеки (см. выше).

## Немного о важном
1. Бот автоматически начинает работу в режиме пересылки, копируя сообщения пользователей.
2. Отправьте команду /start для выбора режима: Опросы или Викторины.
3. 
   1) Выберите опцию "📋 Пройти опрос". <br />
   2) Бот задаёт вопросы последовательно, предоставляя варианты ответов. 
   3) По окончании опроса пользователь получает сообщение об успешном завершении.
4. 
   1) Выберите опцию "🧠 Пройти викторину". <br />
   2) Бот задаёт вопросы, проверяет ответы и уведомляет, правильно ли ответил пользователь. <br />
   3) После завершения викторины бот подсчитывает количество правильных ответов и выводит результат.
5. Отправьте команду /end для выбора режима пересылки сообщений.
6. Enjoy & have fun

## Установка
Для корректной работы кода необходимо установить библиотеки, описанные в файле ___requirements.txt___.

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/Arthicsu/botAnswers.git
2. Устанавливаете все необходимые библиотеки 
   ```bash
   py -m pip install -r requirements.txt
<br />

## Примеры кода
1) Пример кода для пересылки сообщений
```python
@router.message()
async def forward_message(message: Message):
    await message.send_copy(chat_id=message.chat.id)
```

2) Пример кода для обработки вопросов викторины
```python
async def handle_quiz_answer(message: Message, state: FSMContext):
    user_id = message.from_user.id
    step = user_data[user_id]["quiz_step"]
    quiz = quizzes[step]
    correct_option = quiz["options"][quiz["correct_option_id"]]

    if message.text == correct_option:
        await message.answer("Правильно :)")
        user_data[user_id]["correct_answers"] += 1
    else:
        await message.answer(f"Неправильно :(\nПравильный ответ: {correct_option}")

    if step + 1 < len(quizzes):
        user_data[user_id]["quiz_step"] += 1
        await ask_quiz_question(message)
    else:
        await message.answer(f"Викторина окончена! Вы правильно ответили на {user_data[user_id]['correct_answers']} из {len(quizzes)} вопросов.", reply_markup=default_keyboard)

```

## Использование

Запустите файл `main.py` и бот приобретёт небольшой "интеллект" и большое занудство :)

## Лицензия
MIT