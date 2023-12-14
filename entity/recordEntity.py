from flask_sqlalchemy import SQLAlchemy
from config.dbconfig import db


class Record(db.Model):
    __tablename__ = 'record'

    record_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    date = db.Column(db.Date)
    time_start = db.Column(db.Time)
    time_stop = db.Column(db.Time)
    path = db.Column(db.String(255))
    model_result = db.Column(db.Text)
    calls = db.Column(db.Integer)



    # date = db.Column(db.Date, nullable=False)
    # time_start = db.Column(db.Time, nullable=False)
    # time_stop = db.Column(db.Time, nullable=False)
    # path = db.Column(db.String(255), nullable=False)
    # model_result = db.Column(db.ARRAY(db.Integer), nullable=True)
