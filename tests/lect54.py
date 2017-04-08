import unittest

from fixtures.Pulse_api_client import PulseTestApi
from models import Book


class BookRestAPITests(unittest.TestCase):
    def setUp(self):
        self.books_client = PulseTestApi("books")

    def test_create_book(self):
        book = Book(title = "New Book", author = "Super Author")
        response = self.books_client.create_object(book)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), book.get_dict_with_id())
#        self.client.get_book(book)

if __name__ == '__main__':
    unittest.main()