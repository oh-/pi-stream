from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, FileField, MultipleFileField
from wtforms.validators import DataRequired, Length


class AddNewMediaNomenclatureForm(FlaskForm):
    """
    To begin with this is for adding either a TV show, with multiple media
    files, or a movie, with multiple media
    """

    title = StringField(
        'Title',
        validators=[DataRequired(), Length(min=2, max=20)]
    )
    accepted_media = SelectField( 'Accepted media kind, defaults to avi, mp4...etc' )
    submit = SubmitField('Add new media Kind')

class AddNewMediaForm(FlaskForm):
    """
    The base form for adding media.
    """

    media_files = MultipleFileField(
        'Files'
    )
    the_title = StringField(
        'Title',
        validators=[DataRequired(), Length(min=2, max=20)]
    )
    media_type = SelectField(
        'Media type'
    )
    media_thumbnail = FileField(
        'Thumnail'
    )
    #  id = 123,
    #  categories = ['film', 'leo'],
    #  description = 'A movie',
    submit = SubmitField('Upload and create new media item')


