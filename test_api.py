from django.db import connection
from library.models import Book

connection.queries.clear()

books = Book.objects.select_related('author').all()

for book in books:
    print (book.author.first_name)

print (f"Total queries: {len(connection.queries)}")
