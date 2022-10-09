from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database.database import Base
#sqlalchemy models

# class User(Base):
#     __tablename__ = "users"
#
#     id = Column(Integer, primary_key=True, index=True)
#     email = Column(String, unique=True, index=True)
#     hashed_password = Column(String)
#     is_active = Column(Boolean, default=True)
#
#     items = relationship("Item", back_populates="owner")


class Url(Base):
    __tablename__ = "urls"

    hash_url = Column(String, primary_key=True, index=True)
    original_url = Column(String, index=True)

    # owner = relationship("User", back_populates="items")
