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
        print("Record inserted successfully into User table ", cursor.rowcount)
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert data into User table", error)
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
        print("Failed to select data from User table", error)
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
        print("Failed to select first name from User table", error)
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
        print("Failed to select last name from User table", error)
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
         cursor.execute("PRAGMA foreign_keys = ON;")
         count = cursor.execute(sqlite_insert_query, val)
         sqliteConnection.commit()
         print("Record inserted successfully into Bug table ", cursor.rowcount)
         cursor.close()

     except sqlite3.Error as error:
         print("Failed to insert data into Bug table", error)
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
        cursor.execute("PRAGMA foreign_keys = ON;")
        count = cursor.execute(sqlite_insert_query, val)
        sqliteConnection.commit()
        print("Record inserted successfully into SqliteDb_developers table ", cursor.rowcount)
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert data into feature table", error)
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
        cursor.execute("PRAGMA foreign_keys = ON;")
        count = cursor.execute(sqlite_insert_query, val)
        sqliteConnection.commit()
        print("Record inserted successfully into Project table ", len(cursor.fetchall()))
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert data into Project table", error)
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
        cursor.execute("PRAGMA foreign_keys = ON;")
        count = cursor.execute(sqlite_insert_query, val)
        sqliteConnection.commit()
        print("Record inserted successfully into report table ", cursor.rowcount)
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
        sqlite_select_query = "SELECT project_id,project_name FROM project"
        cursor.execute(sqlite_select_query)
        sqliteConnection.commit()
        value = cursor.fetchall()
        print("Records selected successfully from projects table ", len(cursor.fetchall()))
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
        val = (teamNumber, 1, leader)
        cursor.execute("PRAGMA foreign_keys = ON;")
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
        sqlite_select_query = "SELECT user_id, username FROM user, collaborator WHERE collaborator_id = user_id"
        cursor.execute(sqlite_select_query)
        sqliteConnection.commit()
        value = cursor.fetchall()
        print("Records selected successfully from Collaborator table ", len(cursor.fetchall()))
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to select data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")
        return value

def getBugs():
    value = []
    try:
        sqliteConnection = sqlite3.connect('db.sqlite3')
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")
        sqlite_select_query = "SELECT bug_id, bug_date, bug_title, project.project_id, bug_description, project_name, user.username  FROM bug, project, user WHERE bug.project_id = project.project_id AND bug.user_id == user.user_id"
        cursor.execute(sqlite_select_query)
        sqliteConnection.commit()
        value = cursor.fetchall()
        print("Records selected successfully from Bugs table ", len(cursor.fetchall()))
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


def assignUser(team, user):
    noDuplicate = True
    try:
        sqliteConnection = sqlite3.connect('db.sqlite3')
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")
        # verify user isnt already assigned to the project
        sql_verify_query = "Select * FROM works_in WHERE collaborator_id = ? AND team_no = ?"
        cursor.execute(sql_verify_query, (user, team))
        sqliteConnection.commit()
        if len(cursor.fetchall()) != 0:
            noDuplicate = False
            return
        # insert them into the project
        sqlite_insert_query = """INSERT INTO works_in
                                    (collaborator_id, team_no) 
                                    VALUES 
                                    (?,?)"""
        val = (user,team)
        cursor.execute("PRAGMA foreign_keys = ON;")
        count = cursor.execute(sqlite_insert_query, val)
        sqliteConnection.commit()
        cursor.fetchall()
        print("Record inserted successfully into SqliteDb_developers table ", len(cursor.fetchall()))
        # update number of members in team
        sqlite_select_query = "Select count(*) FROM works_in WHERE team_no = ?"
        val = (team,)
        count  = cursor.execute(sqlite_select_query,val)
        sqliteConnection.commit()
        count = cursor.fetchall()[0][0]
        sqlite_update_query = "UPDATE team SET no_people = ? WHERE team_no = ?"
        val = (count, team)
        cursor.execute("PRAGMA foreign_keys = ON;")
        cursor.execute(sqlite_update_query, val)
        sqliteConnection.commit()
        cursor.fetchall()
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")
        return noDuplicate

def getTeams():
    value = []
    try:
        sqliteConnection = sqlite3.connect('db.sqlite3')
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")
        sqlite_select_query = "SELECT team_no FROM team"
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


def updateLeader(team, user):
    try:
        sqliteConnection = sqlite3.connect('db.sqlite3')
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")
        sqlite_update_query = "UPDATE team SET leader_id = ? WHERE team_no = ?"
        val = (user, team)
        cursor.execute("PRAGMA foreign_keys = ON;")
        cursor.execute(sqlite_update_query, val)
        sqliteConnection.commit()
        cursor.fetchall()
        print("Record updated successfully from SqliteDb_developers table ", len(cursor.fetchall()))
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to update data into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")


def assignTeam(team, ID, project):
    try:
        sqliteConnection = sqlite3.connect('db.sqlite3')
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")
        sqlite_insert_query = "INSERT into assigns (team_no, admin_id, project_id) values (?, ?, ?)"
        val = (team, ID, project)
        cursor.execute("PRAGMA foreign_keys = ON;")
        cursor.execute(sqlite_insert_query, val)
        sqliteConnection.commit()
        cursor.fetchall()
        print("Record inserted successfully from SqliteDb_developers table ", len(cursor.fetchall()))
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

def delete_bug(bug_id):
    try:
        sqliteConnection = sqlite3.connect('db.sqlite3')
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")
        sqlite_insert_query = f"DELETE from bug WHERE bug_id = (?)"
        val = (bug_id, )
        cursor.execute("PRAGMA foreign_keys = ON;")
        cursor.execute(sqlite_insert_query, val)
        sqliteConnection.commit()
        print("Deleted bug id: " + str(bug_id))
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to delete data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

def update_bug_title(bug_id, title):
    try:
        sqliteConnection = sqlite3.connect('db.sqlite3')
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")
        sqlite_insert_query = f"UPDATE bug SET bug_title=(?) WHERE bug_id=(?)"
        val = (title, bug_id)
        cursor.execute("PRAGMA foreign_keys = ON;")
        cursor.execute(sqlite_insert_query, val)
        sqliteConnection.commit()
        print("Update bug id: " + str(bug_id))
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to delete data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

def update_bug_description(bug_id, description):
    try:
        sqliteConnection = sqlite3.connect('db.sqlite3')
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")
        sqlite_insert_query = f"UPDATE bug SET bug_description=(?) WHERE bug_id=(?)"
        val = (description, bug_id)
        cursor.execute("PRAGMA foreign_keys = ON;")
        cursor.execute(sqlite_insert_query, val)
        sqliteConnection.commit()
        print("Update bug id: " + str(bug_id))
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to delete data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

def getFeatures():
    value = []
    try:
        sqliteConnection = sqlite3.connect('db.sqlite3')
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")
        sqlite_select_query = "SELECT feature_id, feature_date, feature_title, project.project_id, feature_description, project_name, user.username  FROM feature, project, user WHERE feature.project_id = project.project_id AND feature.user_id == user.user_id"
        cursor.execute(sqlite_select_query)
        sqliteConnection.commit()
        value = cursor.fetchall()
        print("Records selected successfully from feature table ", len(cursor.fetchall()))
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to select data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")
        return value
    
def delete_feature(feature_id):
    try:
        sqliteConnection = sqlite3.connect('db.sqlite3')
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")
        sqlite_insert_query = f"DELETE from feature WHERE feature_id = (?)"
        val = (feature_id, )
        cursor.execute("PRAGMA foreign_keys = ON;")
        cursor.execute(sqlite_insert_query, val)
        sqliteConnection.commit()
        print("Deleted bug id: " + str(feature_id))
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to delete data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

def update_feature_title(feature_id, title):
    try:
        sqliteConnection = sqlite3.connect('db.sqlite3')
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")
        sqlite_insert_query = f"UPDATE feature SET feature_title=(?) WHERE feature_id=(?)"
        val = (title, feature_id)
        cursor.execute("PRAGMA foreign_keys = ON;")
        cursor.execute(sqlite_insert_query, val)
        sqliteConnection.commit()
        print("Update feature id: " + str(feature_id))
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to delete data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

def update_feature_description(feature_id, description):
    try:
        sqliteConnection = sqlite3.connect('db.sqlite3')
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")
        sqlite_insert_query = f"UPDATE feature SET feature_description=(?) WHERE feature_id=(?)"
        val = (description, feature_id)
        cursor.execute("PRAGMA foreign_keys = ON;")
        cursor.execute(sqlite_insert_query, val)
        sqliteConnection.commit()
        print("Update feature id: " + str(feature_id))
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to delete data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

def getUserTickets(user):
    value = []
    try:
        sqliteConnection = sqlite3.connect('db.sqlite3')
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")
        sqlite_select_query = "Select ticket_no FROM works_in, works_on WHERE collaborator_id  = ? AND works_in.team_no = works_on.team_no"
        val = (user,)
        cursor.execute("PRAGMA foreign_keys = ON;")
        cursor.execute(sqlite_select_query, val)
        sqliteConnection.commit()
        value = cursor.fetchall()
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to select data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")
        return value
