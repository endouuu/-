#crudシステムについてのプラグラム
from sqlalchemy.orm import Session
import schemas
from db import models
import db.database

#特定のuser情報取得
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

#userのemail情報取得
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

#user情報取得
def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

#user作成
def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_passwd = user.passwd + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_passwd = fake_hashed_passwd)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return  db_user