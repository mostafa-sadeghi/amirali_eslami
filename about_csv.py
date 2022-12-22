# import csv
# file = open("Book.csv","w")
# file.close()

# with open("data.csv","w") as f:
#     writer = csv.writer(f)
#     writer.writerow(["transaction_id","product_id","price"])
#     writer.writerow(["2001","123","100"])
#     writer.writerow(["2002","12","190"])
#     writer.writerow(["2003","170","170"])
#     writer.writerow(["2004","111","10"])

# with open("data.csv", "r") as f:
#     reader = csv.reader(f)
#     # print(list(reader))
#     for row in reader:
#         print(row)


# JSON javascript object notation
import json
from pathlib import Path
movies = [
    {
        "id": 1,
        "title": "movie1",
        "year": 1998
    },
    {
        "id": 2,
        "title": "movie2",
        "year": 1988
    },
    {
        "id": 3,
        "title": "movie3",
        "year": 2022
    }
]

# Path("movies.txt").write_text(str(movies))
# print(type(movies[0]))
# data = Path("movies.txt").read_text()
# print(data[0])

data = json.dumps(movies)
# print(data)
# print(type(data))

Path("movies.json").write_text(data)

data = Path("movies.json").read_text()
# print(data)
# print(type(data))
movies = json.loads(data)
print(movies)
print(type(movies))
print(movies[0]['title'])
