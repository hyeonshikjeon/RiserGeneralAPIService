# db > crud.py

from sqlalchemy.orm import Session
from .schemas import Announcement, Message, Post
from .models import Announcements, Messages, Posts, Follows
from datetime import datetime, timezone


def create_announcement(
        session: Session,
        announcement: Announcement) -> Announcements:
    db_announcement = Announcements(
        author_id=announcement.author_id,
        class_id=announcement.class_id,
        title=announcement.title,
        content=announcement.content,
        deleted="0",
        created_at=datetime.now(timezone.utc)
    )
    session.add(db_announcement)
    session.commit()
    session.refresh(db_announcement)

    return db_announcement


def update_announcement(
        session: Session,
        announcement_id: int,
        info_update: Announcement) -> Announcements:
    announcement_info = session.query(Announcements).get(announcement_id)

    announcement_info.author_id = announcement_info.author_id
    announcement_info.class_id = info_update.class_id
    announcement_info.title = info_update.title
    announcement_info.content = info_update.content
    announcement_info.deleted = info_update.deleted
    announcement_info.created_at = announcement_info.created_at
    announcement_info.updated_at = datetime.now(timezone.utc)

    session.commit()
    session.refresh(announcement_info)

    return announcement_info


def create_message(
        session: Session,
        message: Message) -> Messages:
    db_message = Messages(
        author_id=message.author_id,
        receiver_id=message.receiver_id,
        title=message.title,
        content=message.content,
        deleted="0",
        created_at=datetime.now(timezone.utc)
    )
    session.add(db_message)
    session.commit()
    session.refresh(db_message)

    return db_message


def update_message(
        session: Session,
        message_id: int,
        info_update: Message) -> Messages:
    message_info = session.query(Messages).get(message_id)

    message_info.author_id = message_info.author_id
    message_info.receiver_id = info_update.receiver_id
    message_info.title = info_update.title
    message_info.content = info_update.content
    message_info.deleted = info_update.deleted
    message_info.created_at = message_info.created_at
    message_info.updated_at = datetime.now(timezone.utc)

    session.commit()
    session.refresh(message_info)

    return message_info


def create_post(
        session: Session,
        post: Post) -> Posts:
    db_post = Posts(
        author_id=post.author_id,
        title=post.title,
        content=post.content,
        deleted="0",
        created_at=datetime.now(timezone.utc)
    )
    session.add(db_post)
    session.commit()
    session.refresh(db_post)

    return db_post


def update_post(
        session: Session,
        post_id: int,
        info_update: Post) -> Posts:
    post_info = session.query(Posts).get(post_id)

    post_info.author_id = post_info.author_id
    post_info.title = info_update.title
    post_info.content = info_update.content
    post_info.deleted = info_update.deleted
    post_info.created_at = post_info.created_at
    post_info.updated_at = datetime.now(timezone.utc)

    session.commit()
    session.refresh(post_info)

    return post_info


def create_follow(
        session: Session,
        follower_id: int,
        followee_id: int) -> Follows:
    db_follow = Follows(
        follower_id=follower_id,
        followee_id=followee_id,
        created_at=datetime.now(timezone.utc)
    )

    session.add(db_follow)
    session.commit()
    session.refresh(db_follow)

    return db_follow
