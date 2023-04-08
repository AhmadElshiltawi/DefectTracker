import sqlite3

def insert_user(first_name, last_name, username, password, email):
    try:
        sqliteConnection = sqlite3.connect('db.sqlite3')
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")

        sqlite_insert_query = """INSERT INTO user
                            (user_id, first_name, last_name, email, username, password) 
                            VALUES 
                            (123,'Jafmes','Jamfes','blah@gfmail.com', 'blaoh', 'blfah')"""

        count = cursor.execute(sqlite_insert_query)
        sqliteConnection.commit()
        print("Record inserted successfully into SqliteDb_developers table ", cursor.rowcount)
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

def add_bug(id, date, title, description, project_id, user_id):
     try:
         sqliteConnection = sqlite3.connect('db.sqlite3')
         cursor = sqliteConnection.cursor()
         print("Successfully Connected to SQLite")

         sqlite_insert_query = """INSERT INTO bug
                             (bug_id, bug_date, bug_title, bug_description, project_id, user_id)
                             VALUES
                             (123,'issue','idk','something@gmail.com', 'blaoh', 'blfah')"""

         count = cursor.execute(sqlite_insert_query)
         sqliteConnection.commit()
         print("Record inserted successfully into SqliteDb_developers table ", cursor.rowcount)
         cursor.close()

     except sqlite3.Error as error:
         print("Failed to insert data into sqlite table", error)
     finally:
         if sqliteConnection:
             sqliteConnection.close()
             print("The SQLite connection is closed")