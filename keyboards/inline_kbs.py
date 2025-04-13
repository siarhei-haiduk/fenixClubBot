from aiogram.types import (InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import InlineKeyboardBuilder

import texts as t
from db_handlers.db_class import get_films

main = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text=t.EVENTS, callback_data='events'),
        InlineKeyboardButton(text=t.SERVICES, callback_data='services'),
        InlineKeyboardButton(text=t.ABOUT_ME, callback_data='aboutMe'),
    ],
], resize_keyboard=True, one_time_keyboard=True)

aboutMe = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text=t.BACK, callback_data='back'),
    ]
], resize_keyboard=True, one_time_keyboard=True)

service = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text=t.TG_BOTS, callback_data='tgBots'),
        InlineKeyboardButton(text=t.BACHATA, callback_data='bachata'),
    ],
    [
        InlineKeyboardButton(text=t.RENT, callback_data='rent'),
        InlineKeyboardButton(text=t.CAR_RENT, callback_data='carRent'),
    ],
    [
        InlineKeyboardButton(text=t.BACK, callback_data='back'),
    ]
], resize_keyboard=True, one_time_keyboard=True)

events = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text=t.STANDARD_PARTY, callback_data='standard')
    ],
    [
        InlineKeyboardButton(text=t.THEME_PARTY, callback_data='theme')
    ],
    [
        InlineKeyboardButton(text=t.CINEMA, callback_data='cinema'),
    ],
    [
        InlineKeyboardButton(text=t.BACK, callback_data='back'),
    ]
], resize_keyboard=True, one_time_keyboard=True)

bachata = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text=t.INDIV, callback_data='indiv'),
        InlineKeyboardButton(text=t.SAMPO, callback_data='sampo'),
    ],
    [
        InlineKeyboardButton(text=t.BACK, callback_data='back'),
    ]
], resize_keyboard=True, one_time_keyboard=True)

cinema = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text=t.FILMS_LIST, callback_data='filmsList'),
        InlineKeyboardButton(text=t.SUGGEST_FILM, callback_data='suggestFilm'),
    ],
    [
        InlineKeyboardButton(text=t.BACK, callback_data='back'),
    ]
], resize_keyboard=True, one_time_keyboard=True)


async def films_list_kb():
    kb = InlineKeyboardBuilder()
    films = await get_films()

    for film in films:
        kb.button(text=f'{film.name}', callback_data=f'film_{film.url}')
    kb.button(text=t.BACK, callback_data='back')
    kb.adjust(2)

    return kb.as_markup()
