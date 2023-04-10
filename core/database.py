import random
import sqlite3

def insert_user(first_name, last_name, username, password, email):
    try:
        sqliteConnection = sqlite3.connect('db.sqlite3')
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")
        id = random.randint(0,999999999)
        data = cursor.execute("SELECT * FROM user WHERE user_id = ?", (id,))
        while True:
            if len(cursor.fetchall()) == 0:
                break
            else:
                id = random.randint(0,999999999)
                data = cursor.execute("SELECT * FROM user WHERE user_id = ?", (id,))

        sqlite_insert_query = """INSERT INTO user
                            (user_id, first_name, last_name, email, username, password) 
                            VALUES 
                            (?, ?, ?, ?, ?, ?)"""
        val = (id,first_name,last_name, email,username, password)
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

def add_bug(date, title, description, project_id, user_id):
     try:
         sqliteConnection = sqlite3.connect('db.sqlite3')
         cursor = sqliteConnection.cursor()
         print("Successfully Connected to SQLite")
         id = random.randint(0,999999999)
         data = cursor.execute("SELECT * FROM bug WHERE bug_id = ?", (id,))
         while True:
            if len(cursor.fetchall()) == 0:
                break
            else:
                id = random.randint(0,999999999)
                data = cursor.execute("SELECT * FROM bug WHERE bug_id = ?", (id,))
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
        id = random.randint(0,999999999)
        data = cursor.execute("SELECT * FROM feature WHERE feature_id = ?", (id,))
        while True:
            if len(cursor.fetchall()) == 0:
                break
            else:
                id = random.randint(0, 999999999)
                data = cursor.execute("SELECT * FROM feature WHERE feature_id = ?", (id,))
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
        id = random.randint(0,999999999)
        data = cursor.execute("SELECT * FROM project WHERE project_id = ?", (id,))
        while True:
            if len(cursor.fetchall()) == 0:
                break
            else:
                id = random.randint(0, 999999999)
                data = cursor.execute("SELECT * FROM project WHERE project_id = ?", (id,))
        sqlite_insert_query = """INSERT INTO project
                                    (project_id, start_date, status, description, admin_id) 
                                    VALUES 
                                    (?,?,?,?, ?)"""
        val = (id, start_date, status, description, admin_id)
        count = cursor.execute(sqlite_insert_query, val)
        sqliteConnection.commit()
        print("Record inserted successfully into SqliteDb_developers table ", len(cursor.fetchall))
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


def getProjects():
    value = []
    try:
        sqliteConnection = sqlite3.connect('db.sqlite3')
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")
        sqlite_select_query = "SELECT project_id FROM project"
        cursor.execute(sqlite_select_query)
        sqliteConnection.commit()
        value = cursor.fetchall()
        print("Record selected successfully from SqliteDb_developers table ", cursor.rowcount)
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to select data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")
        return value
    
def checkdata(data, table_name, condition):
    try:
        sqliteConnection = sqlite3.connect('db.sqlite3')
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")
        sql = "SELECT * FROM " + table_name + " WHERE " + condition + " = ?"
        data = cursor.execute(sql, (data,))
        if len(cursor.fetchall()) == 0: 
            return False
        else:
            return True
        
    except sqlite3.Error as error:
        print("Failed to check data in table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

def checkuser(input_username, input_password):
    try:
        sqliteConnection = sqlite3.connect('db.sqlite3')
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")
        print("check user: ? \npassword: ?",(input_username, input_password))
        sql = "SELECT * FROM user WHERE username = ? AND password = ?"
        data = cursor.execute(sql, (input_username, input_password))
        if len(cursor.fetchall()) == 0: 
            return False
        else:
            return True
        
    except sqlite3.Error as error:
        print("Failed to check data in table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

def getTeam():
    value = []
    try:
        sqliteConnection = sqlite3.connect('db.sqlite3')
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")
        sqlite_select_query = "SELECT team_no FROM team"
        cursor.execute(sqlite_select_query)
        sqliteConnection.commit()
        value = cursor.fetchall()
        print("Record selected successfully from SqliteDb_developers table ", cursor.rowcount)
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to select data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")
        return value

def getUsers():
    value = []
    try:
        sqliteConnection = sqlite3.connect('db.sqlite3')
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")
        sqlite_select_query = "SELECT user_id, first_name FROM user"
        cursor.execute(sqlite_select_query)
        sqliteConnection.commit()
        value = cursor.fetchall()
        print("Record selected successfully from SqliteDb_developers table ", cursor.rowcount)
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to select data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")
        return value