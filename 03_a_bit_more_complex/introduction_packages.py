class Library():

    def __init__(self, title=" ", author_name=" ", book_list=None):
        if book_list is None:
            book_list = {}
        self.book_list = book_list

    def add_book(self, title, author):
        self.book_list[title] = author

    def remove_book(self, title):
        if title in self.book_list:
            del self.book_list[title]

    def search_book(self, title):
        if title in self.book_list:
            result = f"this book is from {self.book_list[title]}"
            return result
        return "the book was not found"

    def show_books(self):
        for title, author in self.book_list.items():
            print("book title:", title, "-", "author name:", author)


def menu(first_time_launching=True):
    if first_time_launching:
        print("Welcome to the library menu")

    print("1.add a book")
    print("2.search for book")
    print("3.show all the books")
    print("4.remove a book")
    print("0.exit")


def user_input():
    choice = int(input("Enter your choice: "))
    return choice


if __name__ == "__main__":
    library = Library()
    menu()
    while True:
        choice = user_input()
        match choice:
            case 1:
                title = input("what is the name of the book?\n")
                author = input("what is the author of the book?")
                library.add_book(title, author)
                print("book successfully added")
            case 2:
                title = input("what is the name of the book you are looking for?")
                print(library.search_book(title))
            case 3:
                library.show_books()
            case 4:
                title = input("what is the name of the book you want to remove?")
                library.remove_book(title)
            case 0:
                print("Goodbye")
                break
            case _:
                print("Invalid choice please try again")
        menu(first_time_launching=False)
