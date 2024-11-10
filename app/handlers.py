from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
import app.keyboards as kb

from app.text import webinar_text
from app.database.requests import set_user

user = Router()

@user.message(CommandStart())
async def cmd_start(message: Message):
    await set_user(message.from_user.id)
    await message.answer(text=webinar_text, reply_markup=kb.main)

@user.message(F.text == 'Купить подписку 📈')
async def echo(message: Message):
    await message.reply('тут пока что нихуя нет, но а так тарифы')

@user.message(F.text == 'Поддержка 🤝')
async def echo(message: Message):
    await message.reply('По всем вопросам, касательно отношений - @lluciferro\n По вопросам работы бота - @seeuagony')
    
@user.callback_query(F.data == 'buy')
async def cmd_buy(callback: CallbackQuery):
    await callback.message.answer('test')