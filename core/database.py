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
        val = (id,first_name,last_name, email,username.lower(), password)
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

def select_user(username):
    try:
        sqliteConnection = sqlite3.connect('db.sqlite3')
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")
        cursor.execute("SELECT * FROM user WHERE username=?", (username,))
        user = cursor.fetchall()
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")
        return user

def select_user_first_name(username):
    try:
        sqliteConnection = sqlite3.connect('db.sqlite3')
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")
        cursor.execute("SELECT first_name FROM user WHERE username=?", (username,))
        first_name = cursor.fetchall()
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")
        return first_name

def select_user_last_name(username):
    try:
        sqliteConnection = sqlite3.connect('db.sqlite3')
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")
        cursor.execute("SELECT last_name FROM user WHERE username=?", (username,))
        last_name = cursor.fetchall()
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")
        return last_name


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

def create_project(start_date, status, description, admin_id,name):
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
                                    (project_id, start_date, status, description, admin_id, project_name) 
                                    VALUES 
                                    (?,?,?,?, ?, ?)"""
        val = (id, start_date, status, description, admin_id, name)
        count = cursor.execute(sqlite_insert_query, val)
        sqliteConnection.commit()
        print("Record inserted successfully into SqliteDb_developers table ", len(cursor.fetchall()))
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
        print("Record selected successfully from SqliteDb_developers table ", len(cursor.fetchall()))
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to select data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")
        return value

def getBugPage():
    value = []
    try:
        sqliteConnection = sqlite3.connect('db.sqlite3')
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")
        sqlite_select_query = "SELECT bug.bug_id, project.project_name, bug.bug_date, bug.bug_title, bug.bug_description, user.username FROM bug, project, user Where bug.project_id = project.project_id AND bug.user_id = user.user_id"
        cursor.execute(sqlite_select_query)
        sqliteConnection.commit()
        for row in cursor.fetchall():
            value.append(row)
        print("Record selected successfully from SqliteDb_developers table ", value)
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to select data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")
        return value

def getProjectPage():
    value = []
    try:
        sqliteConnection = sqlite3.connect('db.sqlite3')
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")
        sqlite_select_query = "SELECT project_id, project_name, start_date, status, description, admin_id FROM project"
        cursor.execute(sqlite_select_query)
        sqliteConnection.commit()
        for row in cursor.fetchall():
            value.append(row)
        print("Record selected successfully from SqliteDb_developers table ", value)
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to select data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")
        return value
    
def getFeaturePage():
    value = []
    try:
        sqliteConnection = sqlite3.connect('db.sqlite3')
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")
        sqlite_select_query = "SELECT feature.feature_id, project.project_name, feature.feature_date, feature.feature_title, feature.feature_description, user.username FROM feature, project, user WHERE feature.project_id = project.project_id AND feature.user_id = user.user_id"
        cursor.execute(sqlite_select_query)
        sqliteConnection.commit()
        for row in cursor.fetchall():
            value.append(row)
        print("Record selected successfully from SqliteDb_developers table ", value)
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to select data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")
        return value
    
def getTicketPage():
    value = []
    try:
        sqliteConnection = sqlite3.connect('db.sqlite3')
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")
        sqlite_select_query = "SELECT ticket_no, author, ticket_date, status, priority FROM ticket"
        cursor.execute(sqlite_select_query)
        sqliteConnection.commit()
        for row in cursor.fetchall():
            value.append(row)
        print("Record selected successfully from SqliteDb_developers table ", value)
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to select data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")
        return value
    
def getReportPage():   
    element = []
    value = []
    try:
        sqliteConnection = sqlite3.connect('db.sqlite3')
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")
        sqlite_select_query = "SELECT * FROM progress_report"
        cursor.execute(sqlite_select_query)
        sqliteConnection.commit()
        tickets = cursor.fetchall()

        
        for no in tickets:
            tickets = []
            tickets.append(no)
            sqlite_select_query = "SELECT progress_date, description FROM progress_contents WHERE ticket_no = ?"
            cursor.execute(sqlite_select_query,(no))
            sqliteConnection.commit()
            for row in cursor.fetchall():
                element.append(row)
            tickets.append(element)
            value.append(element)
        print("Record selected successfully from SqliteDb_developers table ", value)
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
        print("check user: ? \npassword: ?",(input_username.lower(), input_password))
        sql = "SELECT * FROM user WHERE username = ? AND password = ?"
        data = cursor.execute(sql, (input_username.lower(), input_password))
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


def getTickets():
    value = []
    try:
        sqliteConnection = sqlite3.connect('db.sqlite3')
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")
        sqlite_select_query = "SELECT ticket_no FROM ticket"
        cursor.execute(sqlite_select_query)
        sqliteConnection.commit()
        value = cursor.fetchall()
        print("Record selected successfully from SqliteDb_developers table ", len(cursor.fetchall()))
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to select data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")
        return value


def createTeam(leader):
    try:
        sqliteConnection = sqlite3.connect('db.sqlite3')
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")
        teamNumber = random.randint(0, 999999999)
        data = cursor.execute("SELECT * FROM team WHERE team_no = ?", (teamNumber,))
        while True:
            if len(cursor.fetchall()) == 0:
                break
            else:
                id = random.randint(0, 999999999)
                data = cursor.execute("SELECT * FROM team WHERE team_no = ?", (teamNumber,))
        sqlite_insert_query = """INSERT INTO team
                                    (team_no, no_people, leader_id) 
                                    VALUES 
                                    (?,?,?)"""
        val = (teamNumber, 0, leader)
        count = cursor.execute(sqlite_insert_query, val)
        sqliteConnection.commit()
        print("Record inserted successfully into SqliteDb_developers table ", len(cursor.fetchall()))
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

def getCollaborators():
    value = []
    try:
        sqliteConnection = sqlite3.connect('db.sqlite3')
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")
        sqlite_select_query = "SELECT collaborator_id FROM collaborator"
        cursor.execute(sqlite_select_query)
        sqliteConnection.commit()
        value = cursor.fetchall()
        print("Record selected successfully from SqliteDb_developers table ", len(cursor.fetchall()))
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to select data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")
        return value
def select_userID(username):
    try:
        sqliteConnection = sqlite3.connect('db.sqlite3')
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")
        cursor.execute("SELECT user_id FROM user WHERE username=?", (username,))
        user_id = cursor.fetchall()
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")
        return user_id
    
# Temp function to add admin
def add_admin(user_id):
    try:
        sqliteConnection = sqlite3.connect('db.sqlite3')
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")
        
        
        sqlite_insert_query = """INSERT INTO admin
                            (admin_id, no_projects) 
                            VALUES 
                            (?, ?)"""
        val = (user_id, 1)
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