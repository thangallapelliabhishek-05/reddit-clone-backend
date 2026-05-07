from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.schema import CommunityCreate
from app.models.models import Community
from app.database.db import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/communities")
def create_community(
    community: CommunityCreate,
    db: Session = Depends(get_db)
):

    new_community = Community(
        name=community.name,
        description=community.description
    )

    db.add(new_community)
    db.commit()
    db.refresh(new_community)

    return {
        "message": "Community created successfully",
        "community": new_community.name
    }

@router.get("/communities")
def get_communities(db: Session = Depends(get_db)):

    communities = db.query(Community).all()

    return communities