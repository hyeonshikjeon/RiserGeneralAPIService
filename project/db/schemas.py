from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class OurBaseModel(BaseModel):
    class Config:
        orm_mode = True


class Announcement(OurBaseModel):
    announcement_id: Optional[int]
    author_id: int
    class_id: int
    title: str
    content: str
    deleted: Optional[bool]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]


class Message(OurBaseModel):
    message_id: Optional[int]
    author_id: int
    receiver_id: int
    title: str
    content: str
    deleted: Optional[bool]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]


class Post(OurBaseModel):
    post_id: Optional[int]
    author_id: int
    title: str
    content: str
    deleted: Optional[bool]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]


class Follow(OurBaseModel):
    follower_id: int
    followee_id: int
    created_at: Optional[datetime]
