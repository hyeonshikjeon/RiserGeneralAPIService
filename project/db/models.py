from sqlalchemy import Column, BIGINT, TEXT, VARCHAR, CHAR, TIMESTAMP
from .base import Base


class Announcements(Base):
    __tablename__ = "announcement"

    announcement_id = Column(BIGINT, primary_key=True, index=True)
    author_id = Column(BIGINT, nullable=False)
    class_id = Column(BIGINT, nullable=False)
    title = Column(VARCHAR(256))
    content = Column(TEXT)
    deleted = Column(CHAR(1))
    created_at = Column(TIMESTAMP(timezone=True))
    updated_at = Column(TIMESTAMP(timezone=True))


class Messages(Base):
    __tablename__ = "message"

    message_id = Column(BIGINT, primary_key=True, index=True)
    author_id = Column(BIGINT, nullable=False)
    receiver_id = Column(BIGINT, nullable=False)
    title = Column(VARCHAR(256))
    content = Column(TEXT)
    deleted = Column(CHAR(1))
    created_at = Column(TIMESTAMP(timezone=True))
    updated_at = Column(TIMESTAMP(timezone=True))


class Posts(Base):
    __tablename__ = "post"

    post_id = Column(BIGINT, primary_key=True, index=True)
    author_id = Column(BIGINT, nullable=False)
    title = Column(VARCHAR(256))
    content = Column(TEXT)
    deleted = Column(CHAR(1))
    created_at = Column(TIMESTAMP(timezone=True))
    updated_at = Column(TIMESTAMP(timezone=True))


class Follows(Base):
    __tablename__ = "follow"

    follower_id = Column(BIGINT, primary_key=True, index=True)
    followee_id = Column(BIGINT, primary_key=True, index=True)
    created_at = Column(TIMESTAMP(timezone=True))
