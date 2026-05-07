from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.schema import VoteCreate
from app.models.models import Vote
from app.database.db import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/votes")
def create_vote(
    vote: VoteCreate,
    db: Session = Depends(get_db)
):

    new_vote = Vote(
        vote_type=vote.vote_type
    )

    db.add(new_vote)
    db.commit()
    db.refresh(new_vote)

    return {
        "message": "Vote added successfully",
        "vote": new_vote.vote_type
    }

@router.get("/votes")
def get_votes(db: Session = Depends(get_db)):

    votes = db.query(Vote).all()

    return votes