from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class AddNewMediaForm(FlaskForm):
    title = StringField(
        'Title',
        validators=[DataRequired(), Length(min=2, max=20)]
    )
    #  id = 123,
    #  file_location = '/Users/samuel/Movies/Catch Me if You Can-b09x4lxs.mp4',
    #  categories = ['film', 'leo'],
    #  description = 'A movie',
    #  thumbnail_url = 'https://fairytalepictures.files.wordpress.com/2016/02/img_5939-1.jpeg'
    submit = StringField('Upload and create new media item')

