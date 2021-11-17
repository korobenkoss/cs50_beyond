import csv
import os

from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_BOOKS_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    f = open("books_small.csv")
    reader = csv.reader(f)
    for isbn, title, author, year in reader:
        if title == "title":
            continue
        # writer = Author(name=author)
        book = Book(title=title, year=str(year), isbn=isbn, written_by=Author(name=author))
        db.session.add(book)
        # db.session.add(writer)
        print(f"Added book {title} by {author} written in {year}, ISBN number is {isbn}.")
    db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        main()
