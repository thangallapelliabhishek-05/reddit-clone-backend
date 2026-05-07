from sqlalchemy import Column, Integer, String
from app.database.db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)

class Community(Base):
    __tablename__ = "communities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    description = Column(String)

class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)

class Vote(Base):
    __tablename__ = "votes"

    id = Column(Integer, primary_key=True, index=True)
    vote_type = Column(String)