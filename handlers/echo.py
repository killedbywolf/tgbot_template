from aiogram import Dispatcher
from aiogram.types import Message


async def echo(message: Message):
    text = message.text
    await message.answer(f'Вы написали: {text}')


def register_echo(dp: Dispatcher):  # Функция по сути заменяет присвоение декоратора.
    dp.register_message_handler(echo)
