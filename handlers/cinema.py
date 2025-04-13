from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

import keyboards.inline_kbs as kb
import texts as t
from db_handlers.db_class import get_film, add_film
from states.states import Cinema, Event

cinema = Router()


# Cinema/Films logic
@cinema.callback_query(Cinema.info, F.data == 'suggestFilm')
async def cinema_info(call: CallbackQuery, state: FSMContext):
    await call.answer()
    await call.message.edit_reply_markup(None)
    await call.message.answer('Введите название фильма:', reply_markup=None)
    await state.set_state(Cinema.name)


@cinema.message(Cinema.name)
async def cinema_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Cinema.year)
    await message.answer('Введите год выпуска:', reply_markup=None)


@cinema.message(Cinema.year)
async def cinema_year(message: Message, state: FSMContext):
    await state.update_data(year=message.text)
    await state.set_state(Cinema.url)
    await message.answer('Введите ссылку на фильм с сайта kinopoisk:', reply_markup=None)


@cinema.message(Cinema.url)
async def cinema_url(message: Message, state: FSMContext):
    if not message.text.startswith('https://www.kinopoisk.ru/film/'):
        await message.answer('Введённая ссылка некорректна. Повторите ввод:')
        return
    film = await get_film(message.text)
    if film:
        await state.set_state(Cinema.info)
        await message.answer(f'Этот фильм уже присутствует в списке кандидатов на просмотр. Название: {film.name}',
                             reply_markup=kb.cinema)
    else:
        await state.update_data(url=message.text)
        data = await state.get_data()
        await add_film(data)
        await state.set_state(Cinema.info)
        await message.answer('Фильм добавлен в базу кандидатов на просмотр.', reply_markup=kb.cinema)


@cinema.message(Cinema.info, F.text == t.FILMS_LIST)
async def films_list(message: Message, state: FSMContext):
    await state.set_state(Cinema.films)
    await message.answer('Список фильмов для просмотра:', reply_markup=await kb.films_list_kb())


@cinema.callback_query(Cinema.films, F.data.startswith('film_'))
async def film_info(callback: CallbackQuery):
    await callback.message.edit_reply_markup(reply_markup=None)
    await callback.message.answer(callback.data, reply_markup=await kb.films_list_kb())


@cinema.callback_query(Cinema.films, F.data == 'back')
async def film_back(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_reply_markup(reply_markup=None)
    await callback.message.answer('Подробная информация про кинопоказы', reply_markup=kb.cinema)
    await state.set_state(Cinema.info)


@cinema.callback_query(Cinema.info, F.data == 'back')
async def cmd_back_to_events(call: CallbackQuery, state: FSMContext):
    # await print_state(call.message, state) # DEBUG
    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer('Возврат в меню мероприятий', reply_markup=kb.events)
    await state.set_state(Event.cinema)
