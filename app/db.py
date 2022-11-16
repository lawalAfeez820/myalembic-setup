import os

from sqlmodel import SQLModel

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker


from alembic import command, config



DATABASE_URL = "postgresql+asyncpg://postgres:password123@localhost:5432/Basket"
engine = create_async_engine(DATABASE_URL, future=True)
def run_upgrade(connection, cfg):
    cfg.attributes["connection"] = connection
    command.upgrade(cfg, "head")


async def run_async_upgrade():
    async_engine = create_async_engine(DATABASE_URL)
    async with async_engine.begin() as conn:
        await conn.run_sync(run_upgrade, config.Config("alembic.ini"))

async def get_session() -> AsyncSession:
    async_session = sessionmaker(
        engine, class_=AsyncSession, expire_on_commit=False
    )
    async with async_session() as session:
        yield session


