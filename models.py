from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class TodoDB(Base):
    __tablename__ = "todos"  # Veritabanındaki tablonun adı

    # Sütunları tanımlıyoruz
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    completed = Column(Boolean, default=False)