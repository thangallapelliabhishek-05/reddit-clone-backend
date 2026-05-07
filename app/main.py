from fastapi import FastAPI
from app.routers import auth
from app.routers import posts
from app.routers import community
from app.routers import comments
from app.routers import votes

from app.database.db import engine, Base
from app.models.models import User, Post, Community, Comment, Vote

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(posts.router)
app.include_router(community.router)
app.include_router(comments.router)
app.include_router(votes.router)

@app.get("/")
def home():
    return {"message": "Reddit Clone API Running"}