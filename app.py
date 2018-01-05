from flask import Flask, render_template, flash, request, redirect, url_for, send_from_directory, session
from uuid import uuid4
from sqlalchemy.dialects.postgresql.base import UUID
from flask_uuid import FlaskUUID
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import *
from credentials import *
from werkzeug.utils import secure_filename
import os

flask_uuid = FlaskUUID()
app = Flask(__name__, static_url_path='')
flask_uuid.init_app(app)
app.secret_key = 's000 secret!'
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

app.config['POSTGRESQL_DATABASE_USER'] = user
app.config['POSTGRESQL_DATABASE_PASSWORD'] = passwd
app.config['POSTGRESQL_DATABASE_DB'] = db_name
app.config['POSTGRESQL_DATABASE_HOST'] = hostname
port = str(5432)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://'+user+':'+passwd+'@'+hostname+':'+port+'/'+db_name
db = SQLAlchemy(app)

from models import Breed, Image

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/breeds')
def breeds():
    rabbits = Breed.query.all();
    return render_template('breeds.html', rabbits=rabbits)

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
        name = request.form.get('breed')
        idcode = uuid4()
        file = request.files['file']
        print(file)
        filename = file.filename
        destination = "/".join([target,filename])
        print(destination)
        file.save(destination)
        breed = Breed(
            name = name
        )
        try:
            picture = Image(
            idcode = idcode,
            breed = Breed.query.filter_by(name=name).first(),
            fullpath = destination
            )
            db.session.add(picture)
            db.session.commit()
        except:
            errors.append("Unable to add item to database.")
            flash('Not added to Database', 'error')
        flash('Successfully Uploaded Image', 'success')
        return redirect(url_for('upload'))
    return render_template('upload.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
