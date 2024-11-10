from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart

import app.keyboards as kb

user = Router()

@user.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(text="", reply_markup=kb.main)

@user.message(F.text == 'Купить подписку 📈')
async def echo(message: Message):
    await message.reply('тут пока что нихуя нет, но а так тарифы')

@user.message(F.text == 'Поддержка 🤝')
async def echo(message: Message):
    await message.reply('По всем вопросам, касательно отношений - @lluciferro \n По вопросам работы бота - @seeuagony')