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

                #Try to create Cursor
                self.cur = self.db.cursor()
                return True

            except Exception as e:
                print(f"Err: {e}")
                return False

# ===== Getters & Setters =====
    # === Setters ===
    def set_database_path(self, database_path):
        self.database_path = database_path

    # === Getters ===
    def get_database_path(self):
        return self.database_path

    def get_database(self):
        return self.db

    def get_cursor(self):
        return self.cur
