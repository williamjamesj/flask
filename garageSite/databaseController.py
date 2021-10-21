import sqlite3

class databaseConnection():
    def __init__(self,DBname):
        self.connection = sqlite3.connect(DBname,check_same_thread=False)
        return
    def insert(self,type,ip,time,status):
        self.connection.execute("INSERT INTO events (eventType, eventIP, eventTime, eventStatus) VALUES (?,?,?,?)",(type,ip,time,status))
        self.connection.commit()
        return
    def query(self):
        results = self.connection.execute("SELECT * FROM events").fetchall() # Retrieve all of the events.
        return results
