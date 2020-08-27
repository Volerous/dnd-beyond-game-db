from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean

Base = declarative_base()

class DNDGame(Base):

  __tablename__ = "dnd_game"

  id = Column(Integer,
              primary_key=True,
              nullable=False)
  name = Column(String,)