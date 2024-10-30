from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from lexicon.lexicon import LEXICON_RU
from keyboards.keyboard_utils import keyboard
from handlers.other_handlers import BotMode

router = Router()

# Этот хэндлер срабатывает на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        text=LEXICON_RU['/start'],
        reply_markup=keyboard
    )

#хендлер для возврата в режим пересылки
@router.message(Command(commands='end'))
async def end_quiz_poll_mode(message: Message, state: FSMContext):
    await state.set_state(BotMode.copy)
    await message.answer(
        text=LEXICON_RU['/end'],
    )
