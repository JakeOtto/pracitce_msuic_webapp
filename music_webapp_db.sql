-- sql doc for web music db
-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS albums;
DROP SEQUENCE IF EXISTS albums_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS albums_id_seq;
CREATE TABLE albums (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    artist_name VARCHAR(255),
    release_year int
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO albums (title, artist_name, release_year) VALUES ('Black Sabbath', 'Black Sabbath', 1970);
INSERT INTO albums (title, artist_name, release_year) VALUES ('Vulgar Display of Power', 'Pantera', 1992);
INSERT INTO albums (title, artist_name, release_year) VALUES ('South of Heaven ', 'Slayer', 1988);
INSERT INTO albums (title, artist_name, release_year) VALUES ('Master of Puppets ', 'Metallica', 1986);
INSERT INTO albums (title, artist_name, release_year) VALUES ('Rust in Peace', 'Megadeth', 1990);


--# Request:
--POST /albums

--# With body parameters:
--title=Voyage
--release_year=2022
--artist_id=2

--# Expected response (200 OK)
--(No content)
-- Your test should assert that the new album is present in the list of records returned by GET /albums