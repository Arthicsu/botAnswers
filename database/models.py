#опросные вопросы и варианты ответов
polls = [
    {"question": "Любите ли вы учится в БГИТУ?", "options": ["\U0001F44D Конечно да!", "\U0001F928 А есть другой ответ?"], "type": "regular"},
    {"question": "Ваш любимый цвет?", "options": ["\U0001F534 Красный", "\U0001F7E9 Зелёный", "\U0001F537 Синий", "\U0001F534 \U0001F7E9 \U0001F537 Мне нравятся все цвета, поэтому RGB"], "type": "regular"},
    {"question": "Ваш любимый фильм?", "options": ["Матрица", "Интерстеллар", "Начало"], "type": "regular"},
]

# Викторинные вопросы, варианты ответов и правильные ответы
quizzes = [
    {"question": "Столица России?", "options": ["Москва", "Париж", "Берлин"], "correct_option_id": 0},
    {"question": "Какая планета ближе всего к Солнцу?", "options": ["Земля", "Марс", "Меркурий"], "correct_option_id": 2},
    {"question": "2 + 2 * 2?", "options": ["6", "8", "4"], "correct_option_id": 0}
]

user_data = {}