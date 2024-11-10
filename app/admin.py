from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, Filter
from aiogram.fsm.context import FSMContext
from app.states import Newsletter
from app.database.requests import get_users

admin = Router()

class Admin(Filter):
    async def __call__(self, message:Message):
        return message.from_user.id in [554926339, 434914711]
    
@admin.message(Admin(), Command('newsletter'))
async def newsletter(message: Message, state: FSMContext):
    await state.set_state(Newsletter.message)
    await message.answer('Введите сообщение для рассылки.')

@admin.message(Newsletter.message)
async def newsletter_message(message: Message, state: FSMContext):
    await state.clear()
    await message.answer('Рассылка началась')    
    users = await get_users()
    for user in users:
        try:
            await message.send_copy(chat_id=user.tg_id)
        except Exception as ex:
            print(ex)
    await message.answer('Рассылка успешно завершена')
    
    