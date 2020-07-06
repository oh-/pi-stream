from flask import Flask, render_template, flash
from flask_sqlalchemy import SQLAlchemy
from default_data import media_items
from forms import AddNewMediaForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '6b158f4cef97ea0a0ffa20b678c1f70a56d0b071ebdb7ec9fe778c2df158870d'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app) 

class User(db.Model):
    """The User Model"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(120), nullable=False, default='default.jpg') #  Hashed file name
    password = db.Column(db.String(60), nullable=False)
    media = db.relationship('Media', backref='author', lazy=True)

    def __repr__(self):
      return f"User('{self.username}','{self.email}', '{self.image_file}' )"

class Series(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True, nullable=False)
    image_file = db.Column(db.String(60), nullable=False, default='default.jpg')

    seasons = db.relationship('Season', backref='series_title', lazy=True)

    def __repr__(self):
      return f"Series('{self.title}', '{self.image_file}')"

class Season(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    season_number = db.Column(db.Integer())
    image_file = db.Column(db.String(60), nullable=False, default='default.jpg')

    series = db.Column(db.Integer, db.ForeignKey('series.id'), nullable=False)
    episodes = db.relationship('Episode', backref='season_number', lazy=True)

    def __repr__(self):
      return f"Season('{self.season_number}', '{self.image_file}')"

class Media(db.Model):
    """A simple example class"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True, nullable=False)
    image_file = db.Column(db.String(60), nullable=False, default='default.jpg')

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


    def __repr__(self):
      return f"Media('{self.title}', '{self.image_file}', Single?='{self.single}')"


class Episode(Media):
    series = db.Column(db.Integer, db.ForeignKey('season.id'), nullable=True)
    season = db.Column(db.Integer, db.ForeignKey('series.id'), nullable=True)


@app.route('/')
@app.route('/home')
def index():
    return render_template('home.html', media_items=media_items)

@app.route('/media/<int:media_id>')
def show_media(media_id):
    #  media = get_media_details(media_id)
    media = media_items[0]
    return render_template('media-single.html', media=media)

# TODO: add media edit page
#  @app.route('/media/<int:media_id>/edit')
#  def edit_media(media_id):
#      return render_template('edit_media.html', form=AddNewMediaForm())

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = AddNewMediaForm()
    if form.validate_on_submit():
        flash(f'New media submitted: {form.the_name.data}')
        # Could also redirect here using return redirect(url_for('home'))
    return render_template('add.html', form=form)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
