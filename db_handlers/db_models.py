from sqlalchemy import ForeignKey, String, BigInteger
from sqlalchemy.dialects.postgresql import Any
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

from config import DB_URL

engine = create_async_engine(url=DB_URL,
                             echo=True)

async_session = async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id: Mapped[Any] = mapped_column(BigInteger)


class Film(Base):
    __tablename__ = 'films'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(64))
    year: Mapped[int]
    url: Mapped[str] = mapped_column(String(128))
    # description: Mapped[str] = mapped_column(String(256))


async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
