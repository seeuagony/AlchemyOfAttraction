from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Купить доступ 📈'),
        KeyboardButton(text='Поддержка 🤝')]
    ],
    resize_keyboard=True,
    input_field_placeholder='Выберите пункт меню'
)

main_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Купить доступ', callback_data='buy')]]
)