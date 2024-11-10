from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart

from app.text import webinar_text
import app.keyboards as kb

user = Router()

@user.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(text=webinar_text, reply_markup=kb.main_inline)

@user.message(F.text == 'Купить подписку 📈')
async def echo(message: Message):
    await message.reply('тут пока что нихуя нет, но а так тарифы')

@user.message(F.text == 'Поддержка 🤝')
async def echo(message: Message):
    await message.reply('По всем вопросам, касательно отношений - @lluciferro\n По вопросам работы бота - @seeuagony')
    
@user.callback_query(F.data == 'buy')
async def cmd_buy(callback: CallbackQuery):
    await callback.message.answer('test')