# relational databases:
# sqlite
# mysql
# mariadb
# postgresqls
# sqlserver

import sqlite3
import json
from pathlib import Path


movies = json.loads(Path('movies.json').read_text())
# print(type(movies))

# CRUD
# connection = sqlite3.connect("movies.sqlite3")
with sqlite3.connect("movies_db.sqlite3") as conn:
    cursor = conn.cursor()
    command = """CREATE TABLE IF NOT EXISTS MOVIES(id INT,
    title VARCHAR(30),
    year INT
        )
        """
    cursor.execute(command)
    # command = "INSERT INTO Movies VALUES (?,?,?)"
    # for movie in movies:
    #     cursor.execute(command, tuple(movie.values()))

    command = "SELECT id,title FROM Movies"
    # command = "SELECT * FROM Movies"
    result = cursor.execute(command)
    # for record in result:
    #     print(record)

    movies = cursor.fetchall()
    print("-------------------------")
    print(movies)
