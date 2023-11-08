from aiogram.types import ReplyKeyboardMarkup,  KeyboardButton

asosiy_menu = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text='👨‍🎓Профиль'),
            KeyboardButton(text='🪙Мои монеты'),
            KeyboardButton(text='💥Space shop')
        ],
        [
            KeyboardButton(text='🏫О школе'),
            KeyboardButton(text='✍️Оставить отзив')
        ],
    ]

)


