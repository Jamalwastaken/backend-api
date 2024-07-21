#from db import db
from swagger_server.db import db


class Task(db.Model):
    __tablename__ = "task"

    task_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    start_date= db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    completed_at = db.Column(db.Date, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"))


class User(db.Model):
    __tablename__ = "user"

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    username = db.Column(db.String(80), nullable=False)

class Collaborator(db.Model):
    __tablename__ = "collaborator"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    task_id = db.Column(db.Integer, db.ForeignKey("task.task_id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"), nullable=False)

class Subtask(db.Model):
    __tablename__ = "subtask"

    subtask_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    parent_task_id = db.Column(db.Integer,db.ForeignKey("task.task_id"), nullable=False)
    child_task_id = db.Column(db.Integer, db.ForeignKey("task.task_id"), nullable=False)


