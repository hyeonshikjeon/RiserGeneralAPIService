from fastapi import FastAPI, Depends
from fastapi import HTTPException
from db import schemas
from db import models
from db import crud
from sqlalchemy.orm import Session
from sqlalchemy import and_
from db.base import get_db
from mycelery import app as celery_app

app = FastAPI()


@app.get(path="/announcement/", response_model=list[schemas.Announcement])
async def get_announcements(student_id: int, session: Session = Depends(get_db)):
    task = celery_app.send_task('RiserAcademicAPI.tasks.RiserAcademicAPI.tasks.get_course_list_by_student_id',
                                [101])
    class_id = task.get()

    announcement = []

    for c in class_id:
        result = session.query(models.Announcements).filter(
            models.Announcements.class_id == c
        )
        for r in result:
            if r.deleted == "0":
                announcement.append(r)
    return announcement


@app.post(path="/announcement/", response_model=schemas.Announcement)
def create_announcement(announcement_info: schemas.Announcement, session: Session = Depends(get_db)):
    return crud.create_announcement(session, announcement_info)


@app.get(path="/announcement/{announcement_id}", response_model=schemas.Announcement)
async def get_announcement(announcement_id: int, session: Session = Depends(get_db)):
    announcement = session.query(models.Announcements).filter(
        models.Announcements.announcement_id == announcement_id
    ).first()
    if announcement is None or announcement.deleted != "0":
        raise HTTPException(status_code=404, detail="An announcement is not found with the announcement_id.")
    return announcement


@app.put(path="/announcement/{announcement_id}", response_model=schemas.Announcement)
def put_announcement(
        announcement_id: int, new_info: schemas.Announcement, session: Session = Depends(get_db)
):
    announcement = session.query(models.Announcements).filter(
        models.Announcements.announcement_id == announcement_id
    ).first()

    if announcement is None or announcement.deleted != "0":
        raise HTTPException(status_code=404, detail="An announcement is not found with the announcement_id.")
    new_info.deleted = "0"
    announcement_info = crud.update_announcement(session, announcement_id, new_info)
    return announcement_info


@app.delete(path="/announcement/{announcement_id}", response_model=schemas.Announcement)
def delete_announcement(announcement_id: int, session: Session = Depends(get_db)):
    announcement = session.query(models.Announcements).filter(
        models.Announcements.announcement_id == announcement_id
    ).first()

    if announcement is None or announcement.deleted != "0":
        raise HTTPException(status_code=404, detail="An announcement is not found with the announcement_id.")
    announcement.deleted = "1"
    announcement_info = crud.update_announcement(session, announcement_id, announcement)
    return announcement_info


@app.get(path="/message/{message_id}", response_model=schemas.Message)
async def get_message(message_id: int, session: Session = Depends(get_db)):
    message = session.query(models.Messages).filter(
        models.Messages.message_id == message_id
    ).first()
    if message is None or message.deleted != "0":
        raise HTTPException(status_code=404, detail="A message is not found with the message_id.")
    return message


@app.post(path="/message/", response_model=schemas.Message)
def create_message(message_info: schemas.Message, session: Session = Depends(get_db)):
    return crud.create_message(session, message_info)


@app.put(path="/message/{message_id}", response_model=schemas.Message)
def put_message(
        message_id: int, new_info: schemas.Message, session: Session = Depends(get_db)
):
    message = session.query(models.Messages).filter(
        models.Messages.message_id == message_id
    ).first()
    if message is None or message.deleted != "0":
        raise HTTPException(status_code=404, detail="A message is not found with the message_id.")
    new_info.deleted = "0"
    message_info = crud.update_message(session, message_id, new_info)
    return message_info


@app.get(path="/message/", response_model=list[schemas.Message])
async def get_messages(receiver_id: int, session: Session = Depends(get_db)):
    message = []
    result = session.query(models.Messages).filter(
        models.Messages.receiver_id == receiver_id
    )
    for r in result:
        if r.deleted == "0":
            message.append(r)
    return message


@app.delete(path="/message/{message_id}", response_model=schemas.Message)
def delete_message(message_id: int, session: Session = Depends(get_db)):
    message = session.query(models.Messages).filter(
        models.Messages.message_id == message_id
    ).first()
    if message is None or message.deleted != "0":
        raise HTTPException(status_code=404, detail="A message is not found with the message_id.")
    message.deleted = "1"
    message_info = crud.update_message(session, message_id, message)
    return message_info


@app.get(path="/post/{post_id}", response_model=schemas.Post)
async def get_post(post_id: int, session: Session = Depends(get_db)):
    post = session.query(models.Posts).filter(
        models.Posts.post_id == post_id
    ).first()
    if post is None or post.deleted != "0":
        raise HTTPException(status_code=404, detail="A post is not found with the post_id.")
    return post


@app.post(path="/post/", response_model=schemas.Post)
def create_post(post_info: schemas.Post, session: Session = Depends(get_db)):
    return crud.create_post(session, post_info)


@app.put(path="/post/{post_id}", response_model=schemas.Post)
def put_post(
        post_id: int, new_info: schemas.Post, session: Session = Depends(get_db)
):
    post = session.query(models.Posts).filter(
        models.Posts.post_id == post_id
    ).first()
    if post is None or post.deleted != "0":
        raise HTTPException(status_code=404, detail="A post is not found with the post_id.")
    new_info.deleted = "0"
    post_info = crud.update_post(session, post_id, new_info)
    return post_info


@app.get(path="/post/", response_model=list[schemas.Post])
async def get_posts(followee_id: int, session: Session = Depends(get_db)):
    post = []
    result = session.query(models.Posts).filter(
        models.Posts.author_id == followee_id
    )
    for r in result:
        if r.deleted == "0":
            post.append(r)
    return post


@app.delete(path="/post/{post_id}", response_model=schemas.Post)
def delete_post(post_id: int, session: Session = Depends(get_db)):
    post = session.query(models.Posts).filter(
        models.Posts.post_id == post_id
    ).first()
    if post is None or post.deleted != "0":
        raise HTTPException(status_code=404, detail="A post is not found with the post_id.")
    post.deleted = "1"
    post_info = crud.update_post(session, post_id, post)
    return post_info


@app.get(path="/follow/{follower_id}", response_model=list[schemas.Follow])
async def get_followees(follower_id: int, session: Session = Depends(get_db)):
    followee = []
    result = session.query(models.Follows).filter(
        models.Follows.follower_id == follower_id
    )
    for r in result:
        followee.append(r)
    return followee


@app.post(path="/follow/{follower_id}/{followee_id}", response_model=schemas.Follow)
def create_follow(follower_id, followee_id, session: Session = Depends(get_db)):
    if follower_id == followee_id:
        raise HTTPException(status_code=404, detail="The user cannot follow the self.")

    follow = session.query(models.Follows).filter(
        and_(models.Follows.follower_id == follower_id,
             models.Follows.followee_id == followee_id)
    ).first()

    if follow is not None:
        raise HTTPException(status_code=404, detail="The user is already following the target.")

    return crud.create_follow(session, follower_id, followee_id)


@app.delete(path="/follow/{follower_id}/{followee_id}", response_model=schemas.Follow)
def delete_follow(follower_id: int, followee_id: int, session: Session = Depends(get_db)):
    follow = session.query(models.Follows).filter(
        and_(models.Follows.follower_id == follower_id,
             models.Follows.followee_id == followee_id)
    ).first()
    if follow is None:
        raise HTTPException(status_code=404, detail="The user is not currently following the target.")

    session.delete(follow)
    session.commit()

    return follow
