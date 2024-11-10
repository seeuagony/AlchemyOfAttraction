from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, Filter
from aiogram.fsm.context import FSMContext
from app.states import Newsletter

admin = Router()

class Admin(Filter):
    async def __call__(self, message:Message):
        return message.from_user.id in []
    
@admin.message(Admin(), Command('newsletter'))
async def newsletter(message: Message, state: FSMContext):
    await state.set_state(Newsletter.message)
    await message.answer('Введите сообщение для рассылки.')

@admin.message(Newsletter.message)
async def newsletter_message(message: Message, state: FSMContext):
    await message.send_copy()
    
    