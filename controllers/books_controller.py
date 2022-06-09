from flask import Flask, render_template, request, redirect, Blueprint
from models.book import Book
import repositories.author_repository as author_repository
import repositories.book_repository as book_repository

book_blueprint = Blueprint("books", __name__)

#GET
@book_blueprint.route("/books")
def books():
    books = book_repository.select_all()
    return render_template("books/index.html", all_books = books)


#NEW
@book_blueprint.route("/books/new", methods=["GET"])
def new_task():
    authors = author_repository.select_all()
    return render_template("books/new.html", all_authors = authors)

#CREATE
@book_blueprint.route("/books", methods=["POST"])
def create_book():
    title = request.form["title"]
    author_id = request.form["author_id"]
    genre = request.form["genre"]
    author = author_repository.select(author_id)
    book = Book(title, author, genre)
    book_repository.save(book)
    return redirect("/books")

#SHOW
@book_blueprint.route("/books/<id>", methods=["GET"])
def show_book(id):
    found_book = book_repository.select(id)
    return render_template("books/show.html", book = found_book)

#EDIT
@book_blueprint.route("/books/<id>/edit")
def edit_task(id):
    book = book_repository.select(id)
    authors = author_repository.select_all()
    return render_template("books/edit.html", book = book, all_authors = authors)

#UPDATE
@book_blueprint.route("/books/<id>", methods=["POST"])
def update_book(id):
    title = request.form["title"]
    author_id = request.form["author_id"]
    genre = request.form["genre"]
    author = author_repository.select(author_id)
    book = book(title, author, genre, id)
    book_repository.update(book)
    return redirect("/book")

#DELETE
@book_blueprint.route("/books/<id>/delete", methods=["POST"])
def delete_book(id):
    book_repository.delete(id)
    return redirect("/books")
    
