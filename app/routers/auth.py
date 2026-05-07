from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta

from app.schemas.schema import UserCreate, UserLogin
from app.models.models import User
from app.database.db import SessionLocal

router = APIRouter()

SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Password Hash
def hash_password(password: str):
    return pwd_context.hash(password)

# Verify Password
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# Create JWT Token
def create_access_token(data: dict):

    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(hours=1)

    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return encoded_jwt

# Signup API
@router.post("/signup")
def signup(user: UserCreate, db: Session = Depends(get_db)):

    hashed_password = hash_password(user.password)

    new_user = User(
        username=user.username,
        email=user.email,
        password=hashed_password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "User created successfully",
        "username": new_user.username,
        "email": new_user.email
    }

# Login API
@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):

    existing_user = db.query(User).filter(User.email == user.email).first()

    if not existing_user:
        return {"message": "User not found"}

    if not verify_password(user.password, existing_user.password):
        return {"message": "Incorrect password"}

    access_token = create_access_token(
        data={"sub": existing_user.email}
    )

    return {
        "message": "Login successful",
        "access_token": access_token,
        "token_type": "bearer"
    }