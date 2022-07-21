import logging
import asyncio
from config import BOT_TOKEN
from aiogram import Bot, Dispatcher
from handlers.echo import register_echo
from handlers.user import register_user_start


logger = logging.getLogger(__name__)


def register_all_handlers(dp):  # Регистрация всех хендлеров (порядок имеет значение)
    register_user_start(dp)
    register_echo(dp)


async def main():
    bot = Bot(token=BOT_TOKEN, parse_mode='HTML')
    dp = Dispatcher(bot)
    register_all_handlers(dp)

    logging.basicConfig(level=logging.INFO)

    await dp.start_polling(bot)


if __name__ == '__main__':  # Запуск бота
    try:
        asyncio.run(main())
    except (RuntimeError, KeyboardInterrupt):
        logger.error('Bot stoped!')

