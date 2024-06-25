from sqlalchemy import Column, Integer, String
from database import Base


class Ad(Base):
    __tablename__ = "ads"

    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    author = Column(String, index=True)
    views = Column(Integer)
    position = Column(Integer)
