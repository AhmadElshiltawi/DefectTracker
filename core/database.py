import random
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

def add_bug(date, title, description, project_id, user_id):
     try:
         sqliteConnection = sqlite3.connect('db.sqlite3')
         cursor = sqliteConnection.cursor()
         print("Successfully Connected to SQLite")
         id = random.getrandbits(15)
         data = cursor.execute("SELECT * FROM bug WHERE bug_id = ?", (id,))
         #while True:
         print(data.rowcount)
         print(cursor.rowcount)
         if data.rowcount == 0:
            print("reached")
            # break
     #     else:
         #         id = random.getrandbits(10)
         #         data = cursor.execute("SELECT * FROM bug WHERE bug_id = ?", (id,))
         sqlite_insert_query = """INSERT INTO bug
                                     (bug_id, bug_date, bug_title, bug_description, project_id, user_id) 
                                     VALUES 
                                     (?,?,?,?, ?, ?)"""
         val = (id,date,title,description, project_id, user_id)
         count = cursor.execute(sqlite_insert_query, val)
         sqliteConnection.commit()
         print("Record inserted successfully into SqliteDb_developers table ", cursor.rowcount)
         cursor.close()

     except sqlite3.Error as error:
         print("Failed to insert data into sqlite table", error)
     finally:
         if sqliteConnection:
             sqliteConnection.close()
             print("The SQLite connection is closed")

def add_featureRequest(date, title, description, project_id, user_id):
    try:
        sqliteConnection = sqlite3.connect('db.sqlite3')
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")
        id = random.getrandbits(15)
        # need to check that the ID hasnt been used yet still
        sqlite_insert_query = """INSERT INTO feature
                                    (feature_id, feature_date, feature_title, feature_description, project_id, user_id) 
                                    VALUES 
                                    (?,?,?,?, ?, ?)"""
        val = (id, date, title, description, project_id, user_id)
        count = cursor.execute(sqlite_insert_query, val)
        sqliteConnection.commit()
        print("Record inserted successfully into SqliteDb_developers table ", cursor.rowcount)
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

def create_project(start_date, status, description, admin_id):
    try:
        sqliteConnection = sqlite3.connect('db.sqlite3')
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")
        id = random.getrandbits(15)
        # need to check that the ID hasnt been used yet still
        sqlite_insert_query = """INSERT INTO project
                                    (project_id, start_date, status, description, admin_id) 
                                    VALUES 
                                    (?,?,?,?, ?)"""
        val = (id, start_date, status, description, admin_id)
        count = cursor.execute(sqlite_insert_query, val)
        sqliteConnection.commit()
        print("Record inserted successfully into SqliteDb_developers table ", cursor.rowcount)
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

def create_report(ticketNo, description, date):
    try:
        sqliteConnection = sqlite3.connect('db.sqlite3')
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")
        sqlite_insert_query = """INSERT INTO progress_contents
                                    (ticket_no, description, progress_date) 
                                    VALUES 
                                    (?,?,?)"""
        val = (ticketNo, description, date)
        count = cursor.execute(sqlite_insert_query, val)
        sqliteConnection.commit()
        print("Record inserted successfully into SqliteDb_developers table ", cursor.rowcount)
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")