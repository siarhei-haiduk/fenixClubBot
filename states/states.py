from aiogram.fsm.state import State, StatesGroup


class RegExample(StatesGroup):
    name = State()
    number = State()
    location = State()


class Service(StatesGroup):
    name = State()
    number = State()
    location = State()


class Event(StatesGroup):
    cinema = State()
    standard = State()
    theme = State()


class Cinema(StatesGroup):
    info = State()
    films = State()
    name = State()
    year = State()
    url = State()


class Bachata(StatesGroup):
    name = State()
    number = State()
    location = State()


class AboutMe(StatesGroup):
    info = State()
