from pydantic import BaseModel
from typing import List


class AdBase(BaseModel):
    title: str
    author: str
    views: int
    position: int


class AdCreate(AdBase):
    id: int


class Ad(AdBase):
    id: int

    class Config:
        from_attributes = True


class AdCreateList(BaseModel):
    ads: List[AdCreate]
