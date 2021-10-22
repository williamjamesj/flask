import sqlite3 # Imports the built-in SQLite library.

class databaseConnection():
    def __init__(self,DBname): # Connects once to the database when the object is initialised.
        self.connection = sqlite3.connect(DBname,check_same_thread=False) # check_same_thread must be false, otherwise the connection cannot be used across Flask threads.
        return
    def insert(self,type,ip,time,status):
        self.connection.execute("INSERT INTO events (eventType, eventIP, eventTime, eventStatus) VALUES (?,?,?,?)",(type,ip,time,status))
        self.connection.commit() # Commits the changes, saving the new data to the database file.
        return
    def query(self):
        results = self.connection.execute("SELECT * FROM events").fetchall() # Retrieve all of the events.
        return results
