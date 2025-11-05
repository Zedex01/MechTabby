"""
DataManager is designed to be used with ML libraries, thus speed is a priority. 

We do not use pandas... way to slow
"""

class DataManager():
    def __init__(self):
        self.inst = self