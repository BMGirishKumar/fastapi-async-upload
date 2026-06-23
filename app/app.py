from fastapi import FastAPI, Form, HTTPException, File, UploadFile, Depends
from app.schemas import PostCreate
from app.db import Post, get_async_session, create_db_and_tables
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager
from sqlalchemy import select

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield


app=FastAPI(lifespan=lifespan)


@app.post("/upload/")
async def upload_file(
    file: UploadFile = File(...), 
    caption: str = Form(''), 
    session: AsyncSession = Depends(get_async_session)
):
    post = Post(caption=caption, url="dummy_url", file_type="Photo", file_name="dummy_file_name")
    session.add(post)
    await session.commit()
    await session.refresh(post)
    return post

@app.get("/feed")
async def get_feed(session: AsyncSession = Depends(get_async_session)):
    result = await session.execute(select(Post).order_by(Post.created_at.desc()))
    
    # Correct way to fetch scalars asynchronously
    posts = result.scalars().all() 
    
    post_data = []
    for post in posts:
        post_data.append({
            "id": str(post.id),
            "caption": post.caption,
            "url": post.url,
            "file_type": post.file_type,
            "file_name": post.file_name,
            "created_at": post.created_at.isoformat()
        })
    return {"posts": post_data}
    