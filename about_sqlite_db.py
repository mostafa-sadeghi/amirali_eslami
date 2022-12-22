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
print(type(movies))

# connection = sqlite3.connect("movies.sqlite3")
with sqlite3.connect("movies.sqlite3") as conn:
