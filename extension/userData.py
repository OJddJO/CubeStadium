import os
import deta

conn = deta.Deta(os.environ["db_key"])

db = conn.Base("cubestadiumdb")

def insertData(username, data={"pb": None, "ao5": None, "ao12": None, "scrambles": [], "times": [], "list_ao5": [], "list_ao12": []}):
    return db.put({"key": username, "data": data})

def fetchAllData():
    return db.fetch().items

def updateData(username, updates):
    return db.update(updates=updates, key=username)
