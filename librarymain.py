import database_library
import mysql.connector
from issue import Issue
from book import Book
from member import Member
from library_management import LibraryManagement
from menulib import LibraryManagement

conn = mysql.connector.connect(
            host="127.0.0.1",
            user="ombati",
            password="your_password",
            database="library"
     )

cursor = conn.cursor()

database_library.create_tables(cursor)
print("Welcome to ABC School Library Management System Menu!\n"
          "1. continue\n"
          "2. Exit"
          )
option1 = int(input("Enter: "))
while option1 != 2:
     print("Welcome to ABC School Library Management System Menu!\n"
          "1. continue\n"
          "2. Exit"
          )
     option1 = int(input("Enter: "))
     if option1 == 1:
          LibraryManagement.display_menu()
          option = int(input("Enter: "))
          while option != 9:
               if option == 1:
                    member_id = int(input("Enter member ID: "))
                    book_code = int(input("Enter book code: "))
                    Issue.issue_book(member_id, book_code)
                    option = 9
                    

               elif option == 2:
                    member_id = int(input("Enter member ID: "))
                    book_code = int(input("Enter book code: "))
                    Issue.return_book(member_id, book_code)
                    option = 9
                    

               elif option == 3:
                    book_code = int(input("Enter book code: "))
                    new_title = input("Book title: ")
                    new_author = input("Book author: ")
                    Book.modify_book(book_code, new_title, new_author)
                    option = 9
                    

               elif option == 4:
                    book_code = int(input("Enter book code: "))
                    Book.delete_book(book_code)
                    option = 9
                    

               elif option == 5:
                    book_code = int(input("Enter book code: "))
                    title = input("Book title: ")
                    author = input("Book author: ")
                    Book.add_book(book_code, title, author)
                    option = 9

               elif option == 6:
                    member_id = int(input("Member ID: "))
                    name = input("Member name: ")
                    Member.add_member(member_id, name)
                    option = 9

               elif option == 7:
                    member_id = int(input("Member ID: "))
                    new_name = input("Member name: ")
                    Member.modify_member(member_id, new_name)
                    option = 9

               elif option == 8:
                    member_id = int(input("Member ID: "))
                    Member.remove_member(member_id)
                    option = 9
               
               else:
                    option = 9
                    option1 = 2
               



