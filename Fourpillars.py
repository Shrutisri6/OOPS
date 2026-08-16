class Book:
    def __init__(self, book_id):
        self.__book_id = book_id
        self.__borrowed = False

    def is_borrowed(self):
        return self.__borrowed

    def borrow(self):
        self.__borrowed = True

    def return_book(self):
        self.__borrowed = False


class User:
    def __init__(self, user_id):
        self.user_id = user_id
        self.borrowed_count = 0

    def can_borrow(self):
        return self.borrowed_count < self.get_borrow_limit()


class Student(User):
    def get_borrow_limit(self):
        return 2


class Teacher(User):
    def get_borrow_limit(self):
        return 5


class Library:
    def borrow_book(self, user, book):
        if book.is_borrowed():
            print("book is already borrowed.")
        elif not user.can_borrow():
            print("Limit reached")
        else:
            book.borrow()
            user.borrowed_count += 1

    def return_book(self, user, book):
        book.return_book()
        user.borrowed_count -= 1


library = Library()

book1 = Book(101)

student = Student(1)
teacher = Teacher(2)


library.borrow_book(student, book1)
library.borrow_book(teacher, book1)


library.return_book(student, book1)
library.borrow_book(teacher, book1)

