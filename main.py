import asyncio
from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config
from aiogram.fsm.storage.memory import MemoryStorage
from handlers import other_handlers, user_handlers, pq_handlers


async def main():
    config: Config = load_config()
    bot = Bot(token=config.tg_bot.token)

    # Инициализируем память для FSM и диспетчер
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)

    # Регистрируем роутеры
    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)
    dp.include_router(pq_handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


asyncio.run(main())
