# Modelos do SQLAlchemy (Banco de Dados)

from sqlalchemy import Column, Integer, String
from app.core.database import Base

'''class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    full_name = Column(String)'''