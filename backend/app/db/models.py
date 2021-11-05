from db.database import Base
from sqlalchemy.sql.schema import Column
from sqlalchemy import String, Integer


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(String(15))
    email = Column(String(50))
