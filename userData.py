import os
import deta

conn = deta.Deta(os.environ["db_key"])

db = conn.Base("data")

def insertData(username, data={"pb": 0.00, "ao5": 0.00, "ao12": 0.00, "solves": ["None"], "times": [0.00], "list_ao5": [0.00], "list_ao12": [0.00]}):
    return db.put({"key": username, "data": data})

def fetchAllData():
    return db.fetch().items

def updateData(username, updates):
    return db.update(updates=updates, key=username)
