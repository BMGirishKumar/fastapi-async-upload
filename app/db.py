from collections.abc import AsyncGenerator
import uuid
from datetime import datetime

# Import native Uuid so it plays nicely with SQLite locally and Postgres later
from sqlalchemy import Column, String, Text, DateTime, Uuid 
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base

DATABASE_URL = "sqlite+aiosqlite:///./test.db"

# 1. Instantiate the base EXACTLY ONCE
Base = declarative_base()

# 2. Inherit your models from that specific Base instance
class Post(Base):
    __tablename__ = "posts"

    # Swapped to native Uuid for clean SQLite local compatibility
    id = Column(Uuid, primary_key=True, default=uuid.uuid4)
    caption = Column(Text)
    url = Column(String, nullable=False)
    file_type = Column(String, nullable=False)
    file_name = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

engine = create_async_engine(DATABASE_URL, echo=True)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

async def create_db_and_tables():
    async with engine.begin() as conn:
        # 3. Reference the exact same Base metadata registry here
        await conn.run_sync(Base.metadata.create_all)

async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session