import asyncio
from asyncopoisk import KinopoiskAPI
from asyncopoisk.models.enums import SearchOrder, SearchFilmType, FilmType

from config import KINOPOISK_TOKEN


async def get_film_by_id(kp_id: int):
    kp = KinopoiskAPI(token=KINOPOISK_TOKEN)
    # Получаем фильм по id
    film = await kp.films(kp_id)
    return film


async def get_film_by_name(name: str):
    kp = KinopoiskAPI(token=KINOPOISK_TOKEN)
    # Получаем фильм по имени
    film = await kp.films.search_by_keyword(keyword=name)
    return film.films[0]


async def return_film_url(name):
    base_url = 'https://www.kinopoisk.ru'
    film = await get_film_by_name(name)
    match film.type:
        case FilmType.FILM:
            return f'{base_url}/film/{film.film_id}'
        case FilmType.TV_SERIES:
            return f'{base_url}/series/{film.film_id}'
        case _:
            print(f'\nKinopoisk film type:\n{film.type}\n')
            return f'nothing found'


if __name__ == "__main__":
    asyncio.run(get_film_by_id(kp_id=841700))
