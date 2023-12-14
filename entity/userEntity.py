from flask_sqlalchemy import SQLAlchemy
from config.dbconfig import db


class User(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    birthday = db.Column(db.Date, nullable=False)  
    nationality = db.Column(db.String(50), nullable=True)
    weight = db.Column(db.Float(precision=5), nullable=True)
    height = db.Column(db.Float(precision=5), nullable=True)  
    medical_condition = db.Column(db.String(255), nullable=False)

    