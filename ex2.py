from book import Book
library = [
    Book("Евгений Онегин", "Пушкин"),
    Book("Преступление и наказание", "Достоевский"),
    Book("Мастер и Маргарита", "Булгаков")
]

for book in library:
    print(f"{book.name}, {book.author}")
