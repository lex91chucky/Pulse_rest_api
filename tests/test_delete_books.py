from models.books import Book
import pytest



@pytest.fixture()
def book(book_app):
    b = Book(title="For del", author="for_del")
    book_app.create_object(b)
    return b

def test_delete(book_app, book):
    print(book)
    response = book_app.delete_object(book)
    assert response.status_code == 204
