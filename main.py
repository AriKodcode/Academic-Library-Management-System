from book import Book
from user import User
from library import Library


if __name__ == "__main__":
    book1 = Book("Harry potter","j k roling","1",True)
    book2 = Book("Lord the rings","tolkein","2",True)
    book3 = Book("A song of ice and fire","george r r martin", "3",True)
    book4 = Book("the hobbit","tolkein","4",True )
    book5 = Book("The Chronicles of Narnia","author C. S. Lewis","5",True)

    user1 = User("1","ari",[])
    user2 = User("2", "meir", [])
    user3 = User("3", "moti", [])

    library1 = Library({book1.ison:book1},{user1.user_id:user1})
    print(library1.register_user(user2))
    for k, v in library1.users.items():
        print()

