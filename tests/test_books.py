import pytest
from models.books import Book

test_data = [Book(title = "New Book", author = "Super Author"), Book(title = "0", author = "1")]

@pytest.mark.parametrize('book', test_data, ids=[repr(b) for b in test_data])
def test_create_book(book_app, book):
    response = book_app.create_object(book)
    assert response.status_code == 201
    assert response.json() == book.get_dict_with_id()

#def test_create_book_without_author(book_app):
#    book = Book(title = "New Book")
#    response = book_app.create_object(book)
#    assert response.status_code == 201
#    assert response.json() == book.get_dict_with_id()
#    self.assertEqual(response.status_code, 201)
#    self.assertEqual(response.json(), book.get_dict_with_id())
#        self.client.get_book(book)
