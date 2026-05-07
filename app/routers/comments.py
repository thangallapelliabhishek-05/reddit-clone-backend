from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.schema import CommentCreate
from app.models.models import Comment
from app.database.db import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/comments")
def create_comment(
    comment: CommentCreate,
    db: Session = Depends(get_db)
):

    new_comment = Comment(
        content=comment.content
    )

    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)

    return {
        "message": "Comment added successfully",
        "comment": new_comment.content
    }

@router.get("/comments")
def get_comments(db: Session = Depends(get_db)):

    comments = db.query(Comment).all()

    return comments