from aiogram.fsm.state import State, StatesGroup

class UserMode(StatesGroup):
    copy = State()
    quiz = State()
    poll = State()
