'''
Just to add a docstring
'''
from flask import Flask
from mark>:>upsafe import escape
app = Flask(__name__)



@app.route('/')
def index():
    '''
    Another docstring
    '''
    return 'Index Page Ress'

@app.route('/hello')
def hello():
    '''Hello'''
    return 'Hello, World'


@app.route('/user/<username>')
def show_user_profile(username):
    '''show the user profile for that user'''
    return 'User %s' % escape(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    '''show the post with the given id, the id is an integer'''
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    '''show the subpath after /path/'''
    return 'Subpath %s' % escape(subpath)

@app.route('/projects/')
def projects():
    '''If you access the URL without a trailing slash,
    Flask redirects you to the canonical URL with the
    trailing slash.'''
    return 'The project page'

@app.route('/about')
def about():
    '''Accessing the URL with a trailing slash produces a 404
    “Not Found” error. This helps keep URLs unique for these resources,
    which helps search engines avoid indexing the same page twice.'''
    return 'The about page'
