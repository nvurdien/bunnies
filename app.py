from flask import Flask, render_template, request
from flask_recaptcha import ReCaptcha
app = Flask(__name__, static_url_path='')
recaptcha = ReCaptcha(app=app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/breeds')
def breeds():
    return render_template('breeds.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/upload')
def upload():
    if request.method == 'POST' and 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        rec = Photo(filename=filename, user=g.user.id)
        rec.store()
        flash("Ok")
        return redirect(url_for('show', id=rec.id))
    return render_template('upload.html')

def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    init_db()
    print('Initialized the database.')

if __name__ == '__main__':
    app.run()
