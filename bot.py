import logging
import asyncio
from config import BOT_TOKEN
from aiogram import Bot, Dispatcher
from bot_commands import set_bot_commands
from handlers.echo import register_echo
from handlers.user import register_user_start


logger = logging.getLogger(__name__)


def register_all_handlers(dp):  # Регистрация всех хендлеров (порядок имеет значение)
    register_user_start(dp)
    register_echo(dp)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )
    logger.error("Starting bot")

    bot = Bot(token=BOT_TOKEN, parse_mode='HTML')
    dp = Dispatcher(bot)

    register_all_handlers(dp)

    await set_bot_commands(bot)

    try:
        await dp.skip_updates()
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':  # Запуск бота
    asyncio.run(main())
