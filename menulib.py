import mysql.connector
from issue import Issue
from book import Book
from member import Member


conn = mysql.connector.connect(
            host="127.0.0.1",
            user="ombati",
            password="your_password",
            database="library"
        )
cursor = conn.cursor()

class LibraryManagement:

    menu_options = {
        1: "Providing books/journals for reading/reference",
        2: "Returning book/journals",
        3: "Modify book records",
        4: "Delete book records",
        5: "Add new book",
        6: "Add new member",
        7: "Modify member records",
        8: "Remove member",
        9: "Exit"
    }

    @staticmethod
    def display_menu():
        print("\n***** ABC School Library Management System Menu *****")
        for option, description in LibraryManagement.menu_options.items():
            print(f"{option}. {description}")

    @staticmethod
    def execute_option(option):
        if option == 1:
            LibraryManagement.provide_books()
        elif option == 2:
            LibraryManagement.issue_books()
        elif option == 3:
            LibraryManagement.modify_book_records()
        elif option == 4:
            LibraryManagement.delete_book_records()
        elif option == 5:
            LibraryManagement.add_new_member()
        elif option == 6:
            LibraryManagement.modify_member_records()
        elif option == 7:
            LibraryManagement.remove_member()
        elif option == 8:
            print("Exiting Menu...")
            exit()
        else:
            print("Invalid option. Please try again.")

    @staticmethod
    def provide_books():
        if Issue.check_availability(12, cursor):
            print("book available")
            Issue.issue_book(123234, 12)
            print("Providing books/journals for reading/reference...")
        else:
            print("book not available...")
        # Implement providing books functionality

    @staticmethod
    def issue_books():
        print("Issuing books to students...")
        # Implement issuing books functionality

    @staticmethod
    def modify_book_records():
        menu_options2 = {
            "1. Add book",
            "2. Delete book",
            "3. Modify book"
        }
        for key, value in menu_options2.items():
            print(f"{key}: {value}")
        modify_option = int((input("Enter; ")))
        if modify_option == 1:
            sql = "INSERT INTO bookRecord (Title,Author,Bno) VALUES (%s,%s,%s)"
            new_title = input("Enter book title: ")
            new_author = input("Enter author: ")
            book_code = int(input("Enter book code: "))
            val = (new_title, new_author, book_code)
            cursor.execute(sql, val)
            conn.commit()
        elif modify_option == 2:
            book_code = int(input("Enter book code: "))
            Book.delete_book(book_code)

        elif modify_option == 3:
            new_title = input("Enter book title: ")
            new_author = input("Enter author: ")
            book_code = int(input("Enter book code: "))
            Book.modify_book(book_code, new_title, new_author)
        else:
            print("invalid")

        print("Modifying book records...")
        # Implement modifying book records functionality

    @staticmethod
    def delete_book_records():
        book_code = int(input("Enter book code: "))
        Book.delete_book(book_code)
        print("Deleting book records...")
         # Implement deleting book records functionality

    @staticmethod
    def add_new_member():
        member_id = int(input("Enter member ID: "))
        name = input("Enter member name: ")
        Member.add_member(member_id, name)
        print("Adding new member...")
        # Implement adding new member functionality

    @staticmethod
    def modify_member_records():
        member_id = int(input("Enter member ID: "))
        new_name = input("Enter member name: ")
        Member.modify_member(member_id, new_name)
        print("Modifying member records...")
        # Implement modifying member records functionality

    @staticmethod
    def remove_member():
        member_id = int(input("Enter member ID: "))
        Member.remove_member(member_id)
        print("Removing member...")
        # Implement removing member functionality

    @classmethod
    def run(cls):
        while True:
            cls.display_menu()
            choice = int(input("Enter your choice: "))
            cls.execute_option(choice)


if __name__ == "__main__":
    LibraryManagement.run()
