from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Купить подписку 📈'),
        KeyboardButton(text='Поддержка 🤝')]
    ],
    resize_keyboard=True,
    input_field_placeholder='Выберите пункт меню'
)