import mysql.connector
from datetime import datetime, timedelta

class LibraryManagement:
    @staticmethod
    def provide_books():
        print("Providing books/journals for reading/reference...")
        # Implement providing books functionality

    @staticmethod
    def issue_books(member_id, book_code):
        conn = mysql.connector.connect(
            host="localhost",
            user="yourusername",
            password="yourpassword",
            database="Library"
        )
        cursor = conn.cursor()
        try:
            available = LibraryManagement.check_availability(book_code, cursor)
            if available:
                due_date = datetime.now() + timedelta(days=10)
                sql = "INSERT INTO issue (Mno, Bno, DueDate) VALUES (%s, %s, %s)"
                val = (member_id, book_code, due_date)
                cursor.execute(sql, val)
                conn.commit()
                print("Book issued successfully!")
            else:
                print("The book is not available.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def check_availability(book_code, cursor):
        sql = "SELECT * FROM issue WHERE Bno = %s AND ReturnDate IS NULL"
        val = (book_code,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        return len(result) == 0

    @staticmethod
    def modify_book_record():
        print("Modifying book records...")
        # Implement modifying book records functionality

    @staticmethod
    def delete_book_record():
        print("Deleting book records...")
        # Implement deleting book records functionality

    @staticmethod
    def add_member():
        print("Adding new member...")
        # Implement adding new member functionality

    @staticmethod
    def modify_member_record():
        
        print("Modifying member records...")
        # Implement modifying member records functionality

    @staticmethod
    def return_book(member_id, book_code):
        conn = mysql.connector.connect(
            host="localhost",
            user="yourusername",
            password="yourpassword",
            database="Library"
        )
        cursor = conn.cursor()
        try:
            sql = "UPDATE issue SET ReturnDate = %s WHERE Mno = %s AND Bno = %s AND ReturnDate IS NULL"
            val = (datetime.now(), member_id, book_code)
            cursor.execute(sql, val)
            conn.commit()
            print("Book returned successfully.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()
            conn.close()

if __name__ == "__main__":
    LibraryManagement.provide_books()
