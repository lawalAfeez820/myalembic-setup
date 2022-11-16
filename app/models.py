from sqlmodel import SQLModel, Field
from typing import List, Optional
from sqlalchemy import Integer,ForeignKey, Column


class SongBase(SQLModel):
    name: str
    artist: str


class Song(SongBase):
    id: int# = Field(default=None, primary_key=True)


class SongCreate(SongBase):
    pass



class User(SQLModel, table = True):
    id: int = Field(default=None, primary_key=True)
    email: str

class BasketBase(SQLModel):
    product: str
    no_of_product: int
    price_per_kg: Optional[int] =None
    price_per_piece: Optional[int] =None

class Basket(BasketBase, table= True):
    id: int = Field(default=None, primary_key=True)
    owner_id:int = Field(sa_column= Column(Integer, 
    ForeignKey("user.id", ondelete="CASCADE"), nullable= False), default = None)

class email(SQLModel):
    email: str

   