from flask import Flask, render_template, flash
from default_data import media_items
from forms import AddNewMediaForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '6b158f4cef97ea0a0ffa20b678c1f70a56d0b071ebdb7ec9fe778c2df158870d'

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
