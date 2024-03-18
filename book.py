import mysql.connector

class Book:
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
    def add_book(book_code, title, author):
        try:
            conn = mysql.connector.connect(
                host="127.0.0.1",
                user="ombati",
                password="your_password",
                database="library"
            )
            cursor = conn.cursor()
            sql = "INSERT INTO bookRecord (Bno, Title, Author) VALUES (%s, %s, %s)"
            val = (book_code, title, author)
            cursor.execute(sql, val)
            conn.commit()
            print("Book added successfully!")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def modify_book(book_code, new_title, new_author):
        try:
            conn = mysql.connector.connect(
                host="127.0.0.1",
                user="ombati",
                password="your_password",
                database="library"
            )
            cursor = conn.cursor()
            sql = "UPDATE bookRecord SET Title = %s, Author = %s WHERE Bno = %s"
            val = (new_title, new_author, book_code)
            cursor.execute(sql, val)
            conn.commit()
            print("Book details modified successfully!")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def delete_book(book_code):
        try:
            conn = mysql.connector.connect(
                host="127.0.0.1",
                user="ombati",
                password="your_password",
                database="library"
            )
            cursor = conn.cursor()
            sql = "DELETE FROM bookRecord WHERE Bno = %s"
            val = (book_code,)
            cursor.execute(sql, val)
            conn.commit()
            print("Book deleted successfully!")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()
            conn.close()

if __name__ == "__main__":
    book_module = Book()
    # Example usage:
    # book_module.add_book("B001", "Book Title", "Author Name")
    # book_module.modify_book("B001", "New Title", "New Author")
    # book_module.delete_book("B001")
