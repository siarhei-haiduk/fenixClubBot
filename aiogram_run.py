import asyncio

from aiogram.types import BotCommand, BotCommandScopeDefault

from handlers.cinema import cinema
from handlers.user import user
from handlers.admin import admin
from create_bot import bot, dp
from db_handlers.db_models import async_main


# Функция, которая настроит командное меню (дефолтное для всех пользователей)
async def set_commands():
    commands = [BotCommand(command='start', description='Старт')]
    await bot.set_my_commands(commands, BotCommandScopeDefault())


# Функция, которая выполнится когда бот запустится
async def start_bot():
    await async_main()
    await set_commands()


async def main():
    # scheduler.add_job(advertising, 'interval', seconds=15*60, kwargs={'bot': bot})
    # scheduler.add_job(mentioning, 'interval', seconds=1*12, kwargs={'bot': bot})
    # scheduler.start()
    dp.include_routers(cinema, user, admin)
    # dp.include_routers(start_router)
    dp.startup.register(start_bot)

    # запуск бота в режиме long polling при запуске бот очищает все обновления, которые были за его моменты бездействия
    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
