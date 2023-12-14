from flask_sqlalchemy import SQLAlchemy
import pymysql

DATABASE_URI = 'mysql+pymysql://admin:password@snorewise.cjuqmphx39vx.us-east-1.rds.amazonaws.com/snorewise'

db = SQLAlchemy()

def init_app(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
