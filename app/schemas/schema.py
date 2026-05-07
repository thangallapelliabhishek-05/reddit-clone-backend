from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

class PostCreate(BaseModel):
    title: str
    content: str

class CommunityCreate(BaseModel):
    name: str
    description: str

class CommentCreate(BaseModel):
    content: str

class VoteCreate(BaseModel):
    vote_type: str