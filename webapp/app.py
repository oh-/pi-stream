from flask import Flask, render_template

app = Flask(__name__)

media_items = [
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
    media = get_media_details(media_id)
    return render_template('media-single.html', media=media)

@app.route('/add')
def add():
    return render_template('add.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
