from book import Book
from user import User
class Library:
    max_borrow_days = 14

    def __init__(self,books : dict[str,Book], users : dict[str,User]):
        self.books = books
        self.users = users

    def register_user(self,user:User):
        self.users.update({user.user_id:user})
        return self.users

    def add_book(self,book:Book):
        self.books[book.ison] = book
        return self.books

    def perform_borrow(self,user_id:str,isbn:str) -> None:
        if user_id in self.users["user"]:
            print("user in the system")
        else:
            print("user not in the system")

        if isbn in self.books["book"]:
            print("book is available")
        else:
            print("book is not available")
        book = self.books[isbn]
        user = self.users[user_id]
        user.borrow_book(book)
        book.is_available = False

    def perform_return(self, user_id: str, isbn: str) -> None:
        if user_id in self.users["user"]:
            print("user in the system")
        else:
            print("user not in the system")
        if isbn in self.books["book"]:
            print("book is in the library")
        else:
            print("book is not in the library")

        book = self.books[isbn]
        user = self.users[user_id]
        if book.is_available == False:
            user.borrowed_books()
            book.is_available == True
