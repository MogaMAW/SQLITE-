import csv 

from cs50 import SQL

open("moga.db","w").close()

db = SQL("sqlite:///moga.db")

db.execute("CREATE TABLE movies(id INTEGER, title TEXT, PRIMARY KEY(id))")
db.execute("CREATE TABLE movie_genre(movies_id INTEGER,genre_id INTEGER,PRIMARY KEY(genre_id),FOREIGN KEY(movies_id) REFERENCES movies(id))")
db.execute("CREATE TABLE genres(id INTEGER, genre TEXT, PRIMARY KEY(id),FOREIGN KEY(id) REFERENCES movie_genre(genre_id))")

with open("gross movies.csv","r") as file:

    reader = csv.DictReader(file)
    

    for row in reader:
        title = row["Film"].strip().capitalize()
        id= db.execute("INSERT INTO movies(title) VALUES(?)", title)
        
        for Genre in row["Genre"].split(","):
            genre =Genre.strip().capitalize()
            
            genre_id=db.execute("INSERT INTO movie_genre(movies_id)VALUES((SELECT id FROM movies WHERE title=?))",title)
            db.execute("INSERT INTO genres (id, genre)VALUES((SELECT genre_id FROM movie_genre WHERE movies_id=?),?)",genre_id, genre)