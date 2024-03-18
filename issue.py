import mysql.connector
from datetime import datetime, timedelta

class Issue:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="127.0.0.1",
            user="ombati",
            password="your_password",
            database="library"
        )
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.cursor.close()
        self.conn.close()

    @staticmethod
    def issue_book(member_id, book_code):
        conn = mysql.connector.connect(
            host="127.0.0.1",
            user="ombati",
            password="your_password",
            database="library"
        )
        cursor = conn.cursor()
        try:
            if Issue.check_availability(book_code, cursor):
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
        sql = "SELECT Bno FROM issue WHERE Bno = %s AND ReturnDate IS NULL"
        val = (book_code,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        return 1 if len(result) == 0 else 0


    @staticmethod
    def return_book(member_id, book_code):
        conn = mysql.connector.connect(
            host="127.0.0.1",
            user="ombati",
            password="your_password",
            database="library"
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
    # Example usage:
    Issue.issue_book("S001", "B001")
    Issue.return_book("S001", "B001")
