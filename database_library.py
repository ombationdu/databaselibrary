import mysql.connector

conn = mysql.connector.connect(
            host="127.0.0.1",
            user="ombati",
            password="your_password",
            database="library"
     )

cursor = conn.cursor()

def create_tables(cursor):
    # Create bookRecord table
    cursor.execute("""CREATE TABLE IF NOT EXISTS bookRecord (
                        Bno VARCHAR(10) PRIMARY KEY, 
                        Title VARCHAR(255), 
                        Author VARCHAR(255)
                    )""")

    #Create member table
    cursor.execute("""CREATE TABLE IF NOT EXISTS member (
                        Mno VARCHAR(10) PRIMARY KEY, 
                        Name VARCHAR(255)
                    )""")

    # Create issue table
    cursor.execute("""CREATE TABLE IF NOT EXISTS issue (
                        Mno VARCHAR(10), 
                        Bno VARCHAR(10), 
                        DueDate DATE, 
                        ReturnDate DATE, 
                        FOREIGN KEY (Mno) REFERENCES member(Mno), 
                        FOREIGN KEY (Bno) REFERENCES bookRecord(Bno)
                    )""")



    conn.commit()
    conn.close()
