#from db import db
import datetime
from dataclasses import dataclass
from typing import Union

from sqlalchemy import UniqueConstraint

from swagger_server.db import db


@dataclass
class Task(db.Model):
    __tablename__ = "task"

    task_id: int
    title: str
    description: str
    start_date: datetime.date
    end_date: datetime.date
    completed_at: Union[None, datetime.date]
    user_id: int

    task_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    start_date= db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    completed_at = db.Column(db.Date, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"))


@dataclass
class User(db.Model):
    __tablename__ = "user"

    user_id: int
    email: str
    username: str

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(20), nullable=False)
    username = db.Column(db.String(80), nullable=False, unique=True)

@dataclass
class Collaborator(db.Model):
    __tablename__ = "collaborator"

    collaborator_id: int
    task_id: int
    user_id: int

    collaborator_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    task_id = db.Column(db.Integer, db.ForeignKey("task.task_id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"), nullable=False)

    __table_args__ = (
        UniqueConstraint("task_id", "user_id", name="_task_user_uc"),
    )

@dataclass
class Subtask(db.Model):
    __tablename__ = "subtask"

    subtask_id: int
    parent_task_id: int
    child_task_id: int

    subtask_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    parent_task_id = db.Column(db.Integer,db.ForeignKey("task.task_id"), nullable=False)
    child_task_id = db.Column(db.Integer, db.ForeignKey("task.task_id"), nullable=False)

    __table_args__ = (
        UniqueConstraint("parent_task_id", "child_task_id", name="_parent_child_uc"),
    )

