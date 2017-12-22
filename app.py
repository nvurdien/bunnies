from flask import Flask, render_template, flash, request, redirect, url_for, send_from_directory, session
from credentials import user, passwd, db_name, hostname
from werkzeug.utils import secure_filename
import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import types
from sqlalchemy.dialects.mysql.base import MSBinary
from sqlalchemy.schema import Column
import datetime
import uuid


app = Flask(__name__, static_url_path='')
app.secret_key = 's000 secret!'
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

app.config['MYSQL_DATABASE_USER'] = user
app.config['MYSQL_DATABASE_PASSWORD'] = passwd
app.config['MYSQL_DATABASE_DB'] = db_name
app.config['MYSQL_DATABASE_HOST'] = hostname
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://'+user+':'+passwd+'@'+hostname+'/'+db_name
db = SQLAlchemy(app)

class UUID(types.TypeDecorator):
    impl = MSBinary
    def __init__(self):
        self.impl.length = 16
        types.TypeDecorator.__init__(self,length=self.impl.length)

    def process_bind_param(self,value,dialect=None):
        if value and isinstance(value,uuid.UUID):
            return value.bytes
        elif value and not isinstance(value,uuid.UUID):
            raise ValueError('value %s is not a valid uuid.UUID' %value)
        else:
            return None

    def process_result_value(self,value,dialect=None):
        if value:
            return uuid.UUID(bytes=value)
        else:
            return None

    def is_mutable(self):
        return False


id_column_name = "id"

def id_column():
    import uuid
    return Column(id_column_name,UUID(),primary_key=True,default=uuid.uuid4)

class Breed(db.Model):
    __tablename__ = 'breed'
    id = id_column()
    name = db.Column('name', db.String(32))
    images = db.relationship('Image', backref='breed', lazy = True)
    def __init__(self, id, name):
        self.name = name

class Image(db.Model):
    __tablename__ = 'image'
    id = id_column()
    breed = db.Column('breed', db.ForeignKey('breed')) 
    time = db.Column('timestamp', db.DateTime)
    data = db.Column('image', db.LargeBinary)
    def __init__(self, fullpath, breed):
        self.data = fullpath
        self.time = datetime.datetime.now()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/breeds')
def breeds():
    return render_template('breeds.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        target = os.path.join(APP_ROOT, 'data')
        print(target)
        if not os.path.isdir(target):
            os.mkdir(target)

        file = request.files['file']
        print(file)
        filename = file.filename
        destination = "/".join([target,filename])
        print(destination)
        file.save(destination)
        flash('Successfully Uploaded Image', 'success')
        return redirect(url_for('upload'))
    return render_template('upload.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
