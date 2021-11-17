from flask import Flask, render_template, jsonify, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_BOOKS_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/books", methods=["post"])
def books():
    '''List all books.'''
    query_search = request.form.get("search_query")
    print(query_search)
    all_books = Book.query.filter(Book.title.ilike(f"%{query_search}%")).all()
    all_authors = Author.query.filter(Author.name.ilike(f"%{query_search}%")).all()
    return render_template("books.html", books=all_books, authors=all_authors)

@app.route("/book/<int:book_id>")
def book(book_id):
    '''Details about a book.'''
    current_book = Book.query.get(book_id)
    return render_template("book.html", book=current_book)

@app.route("/author/<int:author_id>")
def author(author_id):
    '''Details about an author.'''
    current_author = Author.query.get(author_id)
    print(current_author)
    return render_template("author.html", author=current_author)