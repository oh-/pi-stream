from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = '6b158f4cef97ea0a0ffa20b678c1f70a56d0b071ebdb7ec9fe778c2df158870d'
media_items = [
    {
        'title': 'Modern Family',
        'id': 123,
        'file_name': 'modernfam.S11E01.mp4',
        'thumbnail': 'modernfamily.jpg',
        'type': 'video/mp4',
        'categories': ['tv-series', 'comedy'],
        'description': 'Modern Family',
        'thumbnail_url': 'https://www.citytv.com/wp-content/uploads/2012/11/img-allshows-modern_family-S7.jpg'
    },
    {
        'title': 'Catch Me if you can',
        'id': 123,
        'file_location': '/Users/samuel/Movies/Catch Me if You Can-b09x4lxs.mp4',
        'categories': ['film', 'leo'],
        'description': 'A movie',
        'thumbnail_url': 'https://fairytalepictures.files.wordpress.com/2016/02/img_5939-1.jpeg'
    },
    {
        'title': 'A movie',
        'id': 123,
        'file_location': '/Users/samuel/Movies/Catch Me if You Can-b09x4lxs.mp4',
        'categories': ['film', 'leo'],
        'description': 'A movie',
        'thumbnail_url': 'https://fairytalepictures.files.wordpress.com/2016/02/img_5939-1.jpeg'
    },
    {
        'title': 'A movie',
        'id': 123,
        'file_location': '/Users/samuel/Movies/Catch Me if You Can-b09x4lxs.mp4',
        'categories': ['film', 'leo'],
        'description': 'A movie',
        'thumbnail_url': 'https://fairytalepictures.files.wordpress.com/2016/02/img_5939-1.jpeg'
    },
    {
        'title': 'A movie',
        'id': 123,
        'file_location': '/Users/samuel/Movies/Catch Me if You Can-b09x4lxs.mp4',
        'categories': ['film', 'leo'],
        'description': 'A movie',
        'thumbnail_url': 'https://fairytalepictures.files.wordpress.com/2016/02/img_5939-1.jpeg'
    },
    {
        'title': 'A movie',
        'id': 124,
        'file_location': '/Users/samuel/Movies/Catch Me if You Can-b09x4lxs.mp4',
        'categories': ['film', 'leo'],
        'description': 'A movie',
        'thumbnail_url': 'https://fairytalepictures.files.wordpress.com/2016/02/img_5939-1.jpeg'
    }
]

@app.route('/')
@app.route('/home')
def index():
    return render_template('home.html', media_items=media_items)

@app.route('/media/<int:media_id>')
def show_media(media_id):
    #  media = get_media_details(media_id)
    media = media_items[0]
    return render_template('media-single.html', media=media)

@app.route('/add')
def add():
    return render_template('add.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
