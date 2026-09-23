from abc import ABC, abstractmethod

class LibraryItem(ABC):
    def __init__(self, title, year, isbn):
        self.title = title
        self.year = year
        self.isbn = isbn
        self.is_borrowed = False
    @abstractmethod
    def display_info(self):
        pass

class Book(LibraryItem):
    def __init__ (self, title, author, year, pages, isbn):
        super().__init__(title, year, isbn) #call constructor LibraryItem
        
        self.author = author
        self.pages = pages
        

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Publication year: {self.year}")
        print(f"Pages: {self.pages}")
        print(f"ISBN: {self.isbn}")
        print(f"Borrowed: {self.is_borrowed}")



class Magazines(LibraryItem):
    def __init__(self, title, editor, year, isbn, issue, volume):
        super().__init__(title, year, isbn)

        self.editor = editor
        self.issue = issue
        self.volume = volume

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Editor: {self.editor}")
        print(f"Publication year: {self.year}")
        print(f"ISBN: {self.isbn}")
        print(f"Issue: {self.issue}")
        print(f"Volume: {self.volume}")
        print(f"Borrowed: {self.is_borrowed}")


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    # Work member with book
    def borrow_book(self, book):
        if book not in self.borrowed_books:
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed {book.title}")
        else:
            print("Book already borrowed")

    def return_book(self,book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            print(f"{self.name} returned {book.title}")
        else:
            print("This book is not in borrowed list")

    def show_borrowed_books(self):
        if not self.borrowed_books:
            print("No books borrowed")
        else:
            for book in self.borrowed_books:
                print(book.title)


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    #BOOKS
    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        print("\n-----BOOK LIST-----")
        if not self.books:
            print("No books in library")
        else:
            for index, book in enumerate(self.books, start=1):
                print(f"\nBook #{index}")
                book.display_info()
                print("----------") # show ---- after each bookin a list
        print("---------------\n")

    def find_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None
    
    def return_book(self, member_id, isbn):
        member = self.find_member(member_id)
        book = self.find_book(isbn)

        if member and book:
            member.return_book(book)
            book.is_borrowed = False
        else:
            print("Member or book not found")


    #MEMBERS
    def register_member(self, member):
        self.members.append(member)

    def find_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    #BORROW CONTROL
    def borrow_book(self, member_id, isbn):
        member = self.find_member(member_id)
        book = self.find_book(isbn)
        if member and book:
            if not book.is_borrowed:
                member.borrow_book(book)
                book.is_borrowed = True
            else:
                print("Book already borrowed")
        else:
            print("Member or book not found")



    # View available books
    def show_available_books(self):
        print("\n-----AVAILABLE BOOKS-----")

        found = False

        for index, book in enumerate(self.books, start=1):
            if not book.is_borrowed:
                print(f"\nBook #{index}")
                book.display_info()
                print("----------")
                found = True

        if not found:
            print("No available books")

        print("-------------------------")

    # View borrowed books
    def show_borrowed_books(self):
        print("\n-----BORROWED BOOKS-----")

        found = False

        for index, book in enumerate(self.books, start=1):
            if book.is_borrowed:
                print(f"\nBook #{index}")
                book.display_info()
                print("----------")
                found = True

        if not found:
            print("No borrowed books")

        print("------------------------")
        




library = Library()
while True:
    print("\n=========================")
    print("Library Management System")
    print("=========================")

    print("1. Add Book")
    print("2. Register Member")
    print("3. Show All Books")
    print("4. Show Available Books")
    print("5. Show Borrowed Books")
    print("6. Borrow Book")
    print("7. Return Book")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
       title = input("Title: ")
       author = input("Author: ")
       year = int(input("Year: "))
       pages = int(input("Pages: "))
       isbn = input("ISBN: ")

       new_book = Book(title, author, year, pages, isbn)

       library.add_book(new_book)
       print("Book added successfully")

    elif choice == "2":
       name = input("Member name: ")
       member_id = input("Member ID: ")

       new_member = Member(name, member_id)
       library.register_member(new_member)

       print("Member registered")

    elif choice == "3":
       library.show_books()


    elif choice == "4":
        library.show_available_books()

    elif choice == "5":
        library.show_borrowed_books()


    elif choice == "6":
        member_id = input("Member ID: ")
        isbn = input("ISBN: ")

        library.borrow_book(member_id, isbn)
       

    elif choice == "7":
        member_id = input("Member ID: ")
        isbn = input("ISBN: ")

        library.return_book(member_id, isbn)
    

    elif choice == "8":
       print("Program ending...")
       break

    else:
       print("Invalid option")
