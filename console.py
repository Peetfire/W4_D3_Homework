import pdb
from models.book import Book
from models.author import Author

import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

book_repository.delete_all()
author_repository.delete_all()

author1 = Author("J.R.R. Tolkein")
author_repository.save(author1)
author2 = Author("Iain M. Banks")
author_repository.save(author2)
author3 = Author("Philip K. Dick")
author_repository.save(author3)
author4 = Author("Kurt Vonegut")
author_repository.save(author4)


book1 = Book("Lord of the Rings", "Fantasy", author1, "Penguin") 
book_repository.save(book1)
book2 = Book("The Hobbit", "Fantasy", author1, "penguin")
book_repository.save(book2)