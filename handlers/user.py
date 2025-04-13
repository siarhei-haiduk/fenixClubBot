from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command, CommandObject

import keyboards.inline_kbs as kb
import texts as t
from db_handlers.db_class import set_user
from states.states import AboutMe, Service, Event, Cinema
from utils.kinopoisk import return_film_url, get_film_by_id

user = Router()


@user.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await state.clear()
    await set_user(message.from_user.id)
    await message.answer(t.INIT_TEXT, reply_markup=kb.main)


@user.message(Command('kino'))
async def cmd_rand_kino(message: Message, command: CommandObject):
    args: str = command.args
    url = await return_film_url(args)
    await message.reply(f'Возможно, Вы имели в виду:\n{url}')


@user.message(Command('kino'))
async def cmd_rand_kino(message: Message):
    film = await get_film_by_id(841700)
    await message.answer(f':\n{film.name_ru}')


# About me logic
@user.callback_query(F.data == 'aboutMe')
async def cmd_about_me(call: CallbackQuery, state: FSMContext):
    await call.answer()
    await call.message.edit_reply_markup(None)
    await call.message.answer('Тут будет текст обо мне', reply_markup=kb.aboutMe)
    await state.set_state(AboutMe.info)


# Services logic
@user.callback_query(F.data == 'services')
async def cmd_service(call: CallbackQuery, state: FSMContext):
    await call.answer()
    await call.message.edit_reply_markup(None)
    await call.message.answer('Описание услуг', reply_markup=kb.service)
    await state.set_state(Service.name)


# Events logic
@user.callback_query(F.data == 'events')
async def cmd_events(call: CallbackQuery, state: FSMContext):
    await call.answer()
    await call.message.edit_reply_markup(None)
    await call.message.answer('Описание мероприятий', reply_markup=kb.events)
    await state.set_state(Event.cinema)


@user.callback_query(Event.cinema, F.data == 'cinema')
async def cmd_events(call: CallbackQuery, state: FSMContext):
    await call.answer()
    await call.message.edit_reply_markup(None)
    await call.message.answer('Подробная информация про кинопоказы', reply_markup=kb.cinema)
    await state.set_state(Cinema.info)


# Logic for Back buttons
@user.callback_query(AboutMe.info, F.data == 'back')
@user.callback_query(Service.name, F.data == 'back')
@user.callback_query(Event.cinema, F.data == 'back')
async def cmd_back_to_main(call: CallbackQuery, state: FSMContext):
    # await print_state(call.message, state) # DEBUG
    await state.clear()
    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer('Возврат в главное меню', reply_markup=kb.main)
