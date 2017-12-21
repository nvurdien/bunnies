from flask import Flask, render_template, request, redirect, url_for
from flask_uploads import UploadSet, IMAGES, configure_uploads
from flask_recaptcha import ReCaptcha
from flaskext.mysql import MySQL
from credentials import user, passwd, db_name, hostname
from werkzeug.utils import secure_filename
import os

mysql = MySQL()
app = Flask(__name__, static_url_path='')
recaptcha = ReCaptcha(app=app)
photos = UploadSet('photos', IMAGES)

app.config['MYSQL_DATABASE_USER'] = user
app.config['MYSQL_DATABASE_PASSWORD'] = passwd
app.config['MYSQL_DATABASE_DB'] = db_name
app.config['MYSQL_DATABASE_HOST'] = hostname
app.config['UPLOAD_FOLDER'] = os.getcwd() + 'data/'
mysql.init_app(app)

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
    if 'photo' in request.files:
        file = request.files['photo']
        cursor = mysql.connect().cursor()
        cursor.execute('SELECT UUID_SHORT()')
        uuid = str(cursor.fetchone()[0])

        file.save(os.getcwd() + '/data/' + uuid)
        return redirect(url_for('show', filename=uuid))
    return render_template('upload.html')

if __name__ == '__main__':
    app.run()
