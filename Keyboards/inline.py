from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

language = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Uzb", callback_data="Uzbek"),
            InlineKeyboardButton(text="Eng", callback_data="English"),
            InlineKeyboardButton(text="Rus", callback_data="Russian")
        ],
    ],
)
who = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Ota Onaman', callback_data='ota'),
            InlineKeyboardButton(text='Studentman', callback_data='stud'),
            InlineKeyboardButton(text='Mehmonman', callback_data='meh'),
        ]
    ]
)

important = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('-Mars Airpods-',callback_data='airpods' ),
            InlineKeyboardButton('-Mars Keyboards-',callback_data='keyboards')
        ],
        [
            InlineKeyboardButton('-Mars Powerbank-',callback_data='powerbank'),
            InlineKeyboardButton('-Keyboards Sticker-',callback_data='sticker')
        ],
        [
            InlineKeyboardButton('-Mars Watch-',callback_data='watch'),
            InlineKeyboardButton('-Mars Earphones-',callback_data='earphones')
        ],
        [
            InlineKeyboardButton('-Mars Phone-',callback_data='phone'),
            InlineKeyboardButton('-Mars mini-',callback_data='mars_mini')
        ],
        [
            InlineKeyboardButton('-Mars Sticker-',callback_data='sticker2'),
            InlineKeyboardButton('-Mars notebook-',callback_data='notebook')
        ]
    ]
)
