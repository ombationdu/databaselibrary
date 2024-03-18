from database import Database
from book import Book
from issue import Issue
from member import Member

class LibraryManagementSystem:
    def __init__(self):
        self.database = Database()
        self.book_module = Book()
        self.issue_module = Issue()
        self.member_module = Member()

    def display_menu(self):
        print("\n***** ABC School Library Management System *****")
        print("1. Provide Books/Journals for Reading/Reference")
        print("2. Issue Books to Students/Teachers")
        print("3. Modify Book Records")
        print("4. Delete Book Records")
        print("5. Add New Member")
        print("6. Modify Member Records")
        print("7. Remove Member")
        print("8. Exit")

    def execute_option(self, choice):
        if choice == 1:
            self.book_module.provide_books()
        elif choice == 2:
            member_id = input("Enter Member ID: ")
            book_code = input("Enter Book Code: ")
            self.issue_module.issue_book(member_id, book_code)
        elif choice == 3:
            self.book_module.modify_book_record()
        elif choice == 4:
            self.book_module.delete_book_record()
        elif choice == 5:
            member_id = input("Enter Member ID: ")
            name = input("Enter Member Name: ")
            self.member_module.add_member(member_id, name)
        elif choice == 6:
            member_id = input("Enter Member ID: ")
            new_name = input("Enter New Member Name: ")
            self.member_module.modify_member_record(member_id, new_name)
        elif choice == 7:
            member_id = input("Enter Member ID to remove: ")
            self.member_module.remove_member(member_id)
        elif choice == 8:
            print("Exiting Library Management System...")
            self.database.close_connection()
            exit()
        else:
            print("Invalid choice. Please try again.")

    def run(self):
        while True:
            self.display_menu()
            try:
                choice = int(input("Enter your choice: "))
                self.execute_option(choice)
            except ValueError:
                print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    library_system = LibraryManagementSystem()
    library_system.run()
