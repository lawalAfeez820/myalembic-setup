from fastapi import Depends, FastAPI
from sqlalchemy import select
from sqlmodel import Session
import asyncio

from app.db import get_session, run_async_upgrade
from app.models import Song, SongCreate
from . import models
from fastapi import BackgroundTasks



app = FastAPI()


@app.on_event("startup")
async def on_startup():
    await run_async_upgrade()
   # await init_db()

#asyncio.run(run_async_upgrade())


@app.get("/ping")
async def pong():
    return {"ping": "pong!"}

def write_notification(email: str, message=""):
    with open("log.txt", mode="w") as email_file:
        content = f"notification for {email}: {message}"
        email_file.write(content)

@app.post("/send")
async def send_notification(email: models.User, db: Session = Depends(get_session)):
    db.add(email)
    await db.commit()
    await db.refresh(email)
    
    
    return email


"""@app.get("/songs", response_model=list[Song])
def get_songs(session: Session = Depends(get_session)):
    result = session.execute(select(Song))
    songs = result.scalars().all()
    return [Song(name=song.name, artist=song.artist, id=song.id) for song in songs]"""


@app.post("/post")
async def add_song(items:  models.BasketBase, session: Session = Depends(get_session)):
    items = models.Basket.from_orm(items)
    user = models.User()
    session.add(user)
    await session.commit()
    items.owner_id = user.id
    session.add(items)
    await session.commit()
    await session.refresh(items)
    return items

