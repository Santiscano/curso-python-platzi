import datetime
from sqlalchemy import Column, DateTime, Float, Integer, String
from config.database import Base

class Movie(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    overview = Column(String, index=True)
    year = Column(Integer, index=True)
    rating = Column(Float, index=True)
    category = Column(String, index=True)
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime, default=datetime.datetime.now)