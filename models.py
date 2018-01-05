from uuid import uuid4
from app import db
import datetime
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.dialects.postgresql.base import UUID
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import *
from sqlalchemy.dialects.mysql.base import MSBinary
from sqlalchemy.orm import mapper
from sqlalchemy.schema import Column

db.UUID = UUID

class Breed(db.Model):
    __tablename__ = 'breed'
    id = db.Column(db.UUID(as_uuid=True),primary_key=True,default=uuid4())
    name = db.Column('name', db.String(32))
    images = db.relationship('image', backref='breed', lazy = True)
    def __init__(self, name):
        self.name = name


class Image(db.Model):
    __tablename__ = 'image'
    id = db.Column(db.UUID(as_uuid=True),primary_key=True)
    breed = db.Column('breed', db.ForeignKey('breed'))
    time = db.Column('time', db.DateTime)
    fullpath = db.Column('fullpath', db.String)
    def __init__(self, idcode, fullpath, breed):
        self.id = idcode
        self.fullpath = fullpath
        self.breed = breed
        self.time = datetime.datetime.now()

class Example_Breed(db.Model):
    __tablename__='example_breed'
    breed = db.Column('breed', db.String, primary_key=True)
    path = db.Column('picture_path', db.String)
    desc = db.Column('desc', db.Text)
    def __init__(self, breed, path, desc):
        self.breed = breed
        self.path = path
        self.desc = desc