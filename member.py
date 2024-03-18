import mysql.connector

class Member:
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
    def add_member(member_id, name):
        try:
            conn = mysql.connector.connect(
                host="127.0.0.1",
                user="ombati",
                password="your_password",
                database="library"
            )
            cursor = conn.cursor()
            sql = "INSERT INTO member (Mno, Name) VALUES (%s, %s)"
            val = (member_id, name)
            cursor.execute(sql, val)
            conn.commit()
            print("Member added successfully!")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def modify_member(member_id, new_name):
        try:
            conn = mysql.connector.connect(
                host="127.0.0.1",
                user="ombati",
                password="your_password",
                database="library"
            )
            cursor = conn.cursor()
            sql = "UPDATE member SET Name = %s WHERE Mno = %s"
            val = (new_name, member_id)
            cursor.execute(sql, val)
            conn.commit()
            print("Member details modified successfully!")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def remove_member(member_id):
        try:
            conn = mysql.connector.connect(
                host="127.0.0.1",
                user="ombati",
                password="your_password",
                database="library"
            )
            cursor = conn.cursor()
            sql = "DELETE FROM member WHERE Mno = %s"
            val = (member_id,)
            cursor.execute(sql, val)
            conn.commit()
            print("Member removed successfully!")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()
            conn.close()

if __name__ == "__main__":
    member_module = Member()
    # Example usage:
    # member_module.add_member("S001", "John Doe")
    # member_module.modify_member("S001", "Jane Doe")
    # member_module.remove_member("S001")
