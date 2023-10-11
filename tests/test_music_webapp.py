#adding a new album to list


def test_add_album(db_connection,web_client):
    db_connection.seed("music_webapp_db.sql")

    response = web_client.post("/add", data=
                            {"title":"Voyage",
                            "artist_name": "Jake2",
                            "release_year": 2022})
    
    assert response.status_code == 200

def test_get_artists(db_connection,web_client):
    db_connection.seed("music_webapp_db.sql")
    response = web_client.get("/artists")
    assert response.status_code == 200

def test_post_artists(db_connection,web_client):
    db_connection.seed("music_webapp_db.sql")
    response = web_client.post("/artists", data = {"artist_name":"Sample Artist"})
    assert response.status_code == 200

def test_get_all_albums(db_connection,web_client):
    db_connection.seed("music_webapp_db.sql")
    response = web_client.get("/albums")
    assert response.status_code == 200

    

# # Request:
# POST /albums

# # With body parameters:
# title=Voyage
# release_year=2022
# artist_id=2

# # Expected response (200 OK)
# (No content)
# """
# GET /books/<id>
# """
# def test_get_book(db_connection, web_client):
#     db_connection.seed("seeds/book_store.sql")

#     response = web_client.get("/books/1")

#     assert response.status_code == 200
#     assert response.data.decode("utf-8") == "" \
#         "Book(1, Invisible Cities, Italo Calvino)"

# """
# POST /books
# """
# def test_create_book(db_connection, web_client):
#     db_connection.seed("seeds/book_store.sql")

#     response = web_client.post("/books", data={
#         "title": "The Great Gatsby",
#         "author_name": "F. Scott Fitzgerald"
#     })



