import os
import deta
import streamlit_authenticator as sa

conn = deta.Deta(os.environ["db_key"])

db = conn.Base("users")

def insertUser(name, username, password):
    return db.put({"key": username, "name": name, "password": encodePassword(password)})

def fetchAllUsers():
    return db.fetch().items

def getUser(username):
    return db.get(username)

def updateUser(username, updates):
    return db.update(updates=updates, key=username)

def deleteUser(username):
    return db.delete(username)

def encodePassword(password):
    return sa.Hasher([password]).generate()[0]