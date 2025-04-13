from db_handlers.db_models import async_session
from db_handlers.db_models import User, Film
from sqlalchemy import select


def connection(func):
    async def inner(*args, **kwargs):
        async with async_session() as session:
            return await func(session, *args, **kwargs)

    return inner


@connection
async def set_user(session, tg_id):
    user = await session.scalar(select(User).where(User.tg_id == tg_id))

    if not user:
        session.add(User(tg_id=tg_id))
        await session.commit()


@connection
async def add_film(session, data):
    print(f'\nadd_film data:\n{data}\n')
    film = await session.scalar(select(Film).where((Film.name == data['name']) & (Film.year == data['year'])))

    if not film:
        session.add(Film(name=data['name'], year=data['year'], url=data['url']))
        await session.commit()


@connection
async def get_films(session):
    films = await session.scalars(select(Film).order_by(Film.id))
    films_list = []

    for film in films:
        films_list.append(film)

    return films_list


@connection
async def get_film(session, url):
    film = await session.scalar(select(Film).where(Film.url == url))

    if film:
        print('1')
    else:
        print('2')

    return film
