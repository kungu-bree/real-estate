from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func 

#initialize db/create a new instance
db = SQLAlchemy()

#models

class User(db.Model):
    __tablename__ = 'users'


    id = db.Column(db.Integer,primary_key = True)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, nullable=False, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)
    role = db.Column(db.Text, nullable=False)
    password = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.TIMESTAMP, server_default=db.func.now())
    updated_at = db.Column(db.TIMESTAMP,server_default=db.func.now(),onupdate=db.func.now())
    #isDeleted = db.Column(db.Boolean, server_default=False)
    #soft deleting 
    #deleted_at = db.Column(db.TIMESTAMP)

    #where deleted_at is null

    class LocationModel(db.Model):
        id = db.Column(db.Integer, primary_key = True)
        created_at = db.Column(db.TIMESTAMP, server_default=db.func.now())
        updated_at = db.Column(db.TIMESTAMP, onupdate=db.func.now())

    class PropertyModel(db.Model):
        __tablename__ = 'properties'

        id = db.Column(db.Integer, primary_key = True)
        created_at = db.Column(db.TIMESTAMP, server_default=db.func.now())
        updated_at = db.Column(db.TIMESTAMP,server_default=db.func.now(),onupdate=db.func.now())

