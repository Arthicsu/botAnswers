from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from lexicon.lexicon import LEXICON_RU

router = Router()

class BotMode(StatesGroup):
    copy = State()

# хендлер для текстовых сообщений
@router.message(BotMode.copy, F.text)
async def send_text_echo(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text=LEXICON_RU['no_echo'])
    await message.answer(f"В чат с id = {message.chat.id} поступило текстовое сообщение от {message.from_user.username}")

# Хендлер для фотографий
@router.message(BotMode.copy, F.photo)
async def send_photo_echo(message: Message):
    await message.reply_photo(message.photo[0].file_id)
    await message.answer(f"В чат с id = {message.chat.id} поступила фотография от {message.from_user.username}")

# Хендлер для аудио
@router.message(BotMode.copy, F.audio)
async def send_audio_echo(message: Message):
    await message.reply_audio(message.audio.file_id)
    await message.answer(f"В чат с id = {message.chat.id} поступил аудиофайл от {message.from_user.username}")

# Хендлер для стикеров
@router.message(BotMode.copy, F.sticker)
async def send_sticker_echo(message: Message):
    await message.reply_sticker(message.sticker.file_id)
    await message.answer(f"В чат с id = {message.chat.id} поступил стикер от {message.from_user.username}")

# Хендлер для видео
@router.message(BotMode.copy, F.video)
async def send_video_echo(message: Message):
    await message.reply_video(message.video.file_id)
    await message.answer(f"В чат с id = {message.chat.id} поступило видео от {message.from_user.username}")

# Хендлер для документов
@router.message(BotMode.copy, F.document)
async def send_document_echo(message: Message):
    await message.reply_document(message.document.file_id)
    await message.answer(f"В чат с id = {message.chat.id} поступил документ от {message.from_user.username}")

# Хендлер для анимаций (GIF)
@router.message(BotMode.copy, F.animation)
async def send_animation_echo(message: Message):
    await message.reply_animation(message.animation.file_id)
    await message.answer(f"В чат с id = {message.chat.id} поступила анимация от {message.from_user.username}")

# Хендлер для голосовых сообщений
@router.message(BotMode.copy, F.voice)
async def send_voice_echo(message: Message):
    await message.reply_voice(message.voice.file_id)
    await message.answer(f"В чат с id = {message.chat.id} поступило голосовое сообщение от {message.from_user.username}")

# Хендлер для видеозаметок
@router.message(BotMode.copy, F.video_note)
async def send_video_note_echo(message: Message):
    await message.reply_video_note(message.video_note.file_id)
    await message.answer(f"В чат с id = {message.chat.id} поступила видеозаметка от {message.from_user.username}")