import os
import deta
import streamlit_authenticator as sa

conn = deta.Deta(os.environ["db_key"])

db = conn.Base("cubestadiumdb")

def insertUser(name, username, password, data={"pb": None, "ao5": None, "ao12": None, "scrambles": [], "times": [], "list_ao5": [], "list_ao12": []}):
    return db.put({"key": username, "name": name, "password": encodePassword(password), "data": data})

def fetchAllUsers():
    return db.fetch().items

def updateUser(username, updates):
    return db.update(updates=updates, key=username)

def deleteUser(username):
    return db.delete(username)

def encodePassword(password):
    return sa.Hasher([password]).generate()[0]
