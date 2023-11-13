import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ChatActions
from filters import IsGroup
from loader import dp
@dp.message_handler(IsGroup(), content_types=types.ContentType.NEW_CHAT_MEMBERS)
async def on_user_joined(message: types.Message):
    await message.delete()

@dp.message_handler(IsGroup(), content_types=types.ContentType.LEFT_CHAT_MEMBER)
async def on_user_joined(message: types.Message):
    await message.delete()
