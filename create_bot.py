import logging
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from decouple import config


# from apscheduler.schedulers.asyncio import AsyncIOScheduler
#
# from texts import TEXT_HOME, TEXT_MANAGER, TEXT_CONSULTANT, TEXT_AVITO, TEXT_EFIN, TEXT_ALFABANK, TEXT_YANDEX_COURIER, \
#     TEXT_TBANK

# from db_handler.db_class import PostgresHandler

# pg_db = PostgresHandler(config('PG_LINK'))
# scheduler = AsyncIOScheduler(timezone='Europe/Moscow')
admins = [int(admin_id) for admin_id in config('ADMINS').split(',')]
kinopoisk_token = config('KINOPOISK_TOKEN')

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

bot = Bot(token=config('TOKEN'), default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(storage=MemoryStorage())
