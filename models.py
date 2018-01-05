from app import db
from uuid import uuid4
import datetime
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.dialects.postgresql.base import UUID
from sqlalchemy.dialects.mysql.base import MSBinary
from sqlalchemy.orm import mapper
from sqlalchemy.schema import Column, Table

db.UUID = UUID

class Breed(db.Model):
    __tablename__ = 'breed'
    id = db.Column(db.UUID(as_uuid=True),primary_key=True,default=uuid4())
    name = db.Column('name', db.String(32))
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
