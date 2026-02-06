import sqlite3

class SimpleSQL:
    def __init__(self, database_path=None):
        #Fields
        self.database_path = None
        self.db = None
        self.cur = None

        #If there is no instance of the db
        if self.db is None:
            #If a path was provided in constructor, link to db
            if database_path is not None:
                self.database_path = database_path
                self.connect_database()
    
# ===== Functions & Methods =====

    def get_tables(self):
        return self.db.execute("PRAGMA database_list;").fetchall()

    def get_all(self):
        self.cur.execute("""
            SELECT * FROM timesheet;
            """)
        
        for row in self.cur.fetchall():
            print(row)
    
    #Create Table
    def create_table(self):
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS timesheet (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        project TEXT NOT NULL,
        hours REAL NOT NULL,
        ticket TEXT,
        location TEXT,
        summary TEXT)""")


    def add_entry(self, date, project, hours, ticket=None, location=None, summary=None):
        self.cur.execute("""
            INSERT INTO timesheet (date, project, hours, ticket, location, summary)
            VALUES(?,?,?,?,?,?)
            """, (date, project, hours, ticket, location, summary))
        self.db.commit()

    #Insert
    #Modify
    #Remove
    #Get


    #Connect to db and get cursor
    def connect_database(self, database_path=None) -> bool:
        
        if database_path is not None:
            self.database_path = database_path
        
        #Only ever create one instance of a connection
        if self.db is None:
            try:
               
                self.db = sqlite3.connect(self.database_path)
                print("Connected to db")
                #Try to create Cursor
                self.cur = self.db.cursor()
                print("Assigned Cursor")
                return True

            except Exception as e:
                print(f"Err: {e}")
                return False


