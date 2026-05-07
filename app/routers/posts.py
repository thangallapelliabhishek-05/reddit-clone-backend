from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.schema import PostCreate
from app.models.models import Post
from app.database.db import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/posts")
def create_post(post: PostCreate, db: Session = Depends(get_db)):

    new_post = Post(
        title=post.title,
        content=post.content
    )

    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return {
        "message": "Post created successfully",
        "title": new_post.title
    }

@router.get("/posts")
def get_posts(db: Session = Depends(get_db)):

    posts = db.query(Post).all()

    return posts