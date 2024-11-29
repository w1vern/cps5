from sqlalchemy.ext.asyncio import (
    AsyncConnection,
    AsyncSession,
    async_sessionmaker,
    create_async_engine
)
from sqlalchemy.orm import DeclarativeBase

import contextlib
from typing import Any, AsyncIterator

# Загрузка переменных окружения

# URL для SQLite
DATABASE_URL = "sqlite+aiosqlite:///.db"

# Базовый класс для моделей
class Base(DeclarativeBase):
    pass


class DatabaseSessionManager:
    def __init__(self, host: str, engine_kwargs: dict[str, Any] = {}):
        # Создание асинхронного подключения
        self._engine = create_async_engine(
            host, connect_args={"check_same_thread": False}, **engine_kwargs
        )
        self._session_maker = async_sessionmaker(
            bind=self._engine, expire_on_commit=False
        )

    async def close(self):
        if self._engine is None:
            raise Exception("DatabaseSessionManager is not initialized")
        await self._engine.dispose()
        self._engine = None
        self._session_maker = None

    @contextlib.asynccontextmanager
    async def connect(self) -> AsyncIterator[AsyncConnection]:
        if self._engine is None:
            raise Exception("DatabaseSessionManager is not initialized")

        async with self._engine.begin() as connection:
            try:
                yield connection
            except Exception:
                await connection.rollback()
                raise

    @contextlib.asynccontextmanager
    async def session(self) -> AsyncIterator[AsyncSession]:
        if self._session_maker is None:
            raise Exception("DatabaseSessionManager is not initialized")

        session = self._session_maker()
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()


# Создание менеджера сессий
session_manager = DatabaseSessionManager(DATABASE_URL, {"echo": False})


# Генератор для получения сессии
async def get_db_session():
    async with session_manager.session() as session:
        yield session


# Создание базы данных и таблиц
async def create_db_and_tables():
    async with session_manager.connect() as conn:
        await conn.run_sync(Base.metadata.create_all)
