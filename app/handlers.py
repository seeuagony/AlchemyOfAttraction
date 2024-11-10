from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart

import app.keyboards as kb

user = Router()

@user.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(text="Приветули", )