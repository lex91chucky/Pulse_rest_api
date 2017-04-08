from models.books import Book


def test_create_book(book_app):
    book = Book(title = "New Book", author = "Super Author")
    response = book_app.create_object(book)
    assert response.status_code == 201
    assert response.json() == book.get_dict_with_id()

def test_create_book_without_author(book_app):
    book = Book(title = "New Book")
    response = book_app.create_object(book)
    assert response.status_code == 201
    assert response.json() == book.get_dict_with_id()
#    self.assertEqual(response.status_code, 201)
 #   self.assertEqual(response.json(), book.get_dict_with_id())
#        self.client.get_book(book)
