Search engineee

class Book:
    def __init__(self, isbn, author, title, publisher, genre, year_published, date_purchased, status):
        self.isbn = isbn
        self.author = author
        self.title = title
        self.publisher = publisher
        self.genre = genre
        self.year_published = year_published
        self.date_purchased = date_purchased
        self.status = status

def search_books(books, keyword):
    results = []
    for book in books:
        if keyword.lower() in [book.isbn.lower(), book.author.lower(), book.title.lower()]:
            results.append(book)
    return results

def display_book_details(book):
    print("ISBN:", book.isbn)
    print("Author:", book.author)
    print("Title:", book.title)
    print("Publisher:", book.publisher)
    print("Genre:", book.genre)
    print("Year Published:", book.year_published)
    print("Date Purchased:", book.date_purchased)
    print("Status:", book.status)
    print()

# Example usage:
# Create some book instances
book1 = Book("1234567890", "Brandonnn", "Python and snakes", "PublisherA", "Programming", 2020, "2023-01-01", "Available")
book2 = Book("0987654321", "Beksbeksbeks", "why russian coding is superior", "PublisherB", "Data Science", 2021, "2023-02-15", "Checked Out")
book3 = Book("0123012301", "johnlegend", "all of me", "PublisherC", "Web music", 2019, "2023-03-20", "Ongoing")

# Store books in a list
books_list = [book1, book2, book3]

# Search for books by ISBN, author, or title
search_keyword = input("Enter ISBN, author, or title to search for: ")
search_results = search_books(books_list, search_keyword)

# Display the details of the matching books
if search_results:
    for result in search_results:
        display_book_details(result)
else:
    print("No matching books found.")