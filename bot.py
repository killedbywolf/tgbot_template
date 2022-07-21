import logging
from config import BOT_TOKEN
from aiogram import Bot, Dispatcher, executor
from handlers.echo import register_echo
from handlers.user import register_user_start


def register_all_handlers(dp):  # Регистрация всех хендлеров (порядок имеет значение)
    register_user_start(dp)
    register_echo(dp)


def main():
    bot = Bot(token=BOT_TOKEN, parse_mode='HTML')
    dp = Dispatcher(bot)
    logging.basicConfig(level=logging.INFO)
    register_all_handlers(dp)   # Запуск всех хендлеров
    executor.start_polling(dp)


if __name__ == '__main__':  # Запуск бота
    main()