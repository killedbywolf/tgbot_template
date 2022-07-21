from aiogram import Dispatcher
from aiogram.types import Message


async def user_start(message: Message):
    user = message.from_user.first_name
    await message.answer(f'Hello, {user}')


def register_user_start(dp: Dispatcher):    # Функция по сути заменяет присвоение декоратора.
    dp.register_message_handler(user_start, commands=['start'])
