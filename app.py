import os
from flask import Flask, request, render_template
from lib.album_repository import *
from lib.database_connection import get_flask_database_connection

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# == Example Code Below ==

# GET /emoji
# Returns a emojiy face
# Try it:
#   ; curl http://127.0.0.1:5001/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    return ":)"

@app.route('/albums', methods=['GET'])
def all_albums():
    connection = get_flask_database_connection(app)
    album_repo = Albums_Repository(connection)
    albums = album_repo.all()
    print(type(albums))
    
    return albums
    return render_template("index.html", albums=albums)

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

@app.route('/add', methods = ['POST'])
def add_album():
    title = request.form ['title']
    artist_name = request.form ['artist_name']
    release_year = request.form ['release_year']
    connection = get_flask_database_connection(app)
    album_repo = Albums_Repository(connection)
    album_repo.create(title,artist_name,release_year)
    return f" added  - {title},{artist_name},{release_year}"


#     response = web_client.post("/albums", data=
#                             {"title":"Voyage",
#                             "artist_name": "Jake2",
#                             "release_year": 2022})
#     assert response.status_code == 200