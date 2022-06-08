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
