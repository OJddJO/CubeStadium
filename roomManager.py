import os
import deta

conn = deta.Deta(os.environ["db_key"])
db = conn.Base("cubestadium_pvpRoom")

def createRoom(roomName, user, password, maxUsers, scramble):
    roomData = {
        "key": roomName,
        "admin": user,
        "password": password,
        "userNb": 1,
        "maxUsers": maxUsers,
        "users": [
            {
                "username": user,
                "time": None
            }
        ],
        "status": "waiting",
        "scramble": scramble,
        "winner": None
    }
    return db.put(roomData)

def fetchAllRooms():
    return db.fetch().items

def updateRoom(roomName, updates):
    return db.update(updates=updates, key=roomName)

def leaveRoom(roomName, user):
    room = db.get(roomName).items[0]
    newUsers = []
    for u in room["users"]:
        if u["username"] != user:
            newUsers.append(u)
    userNb = room["userNb"] - 1
    if user == room["admin"]:
        return db.delete(roomName)
    else:
        return db.update(updates={"users": newUsers, "userNb": userNb}, key=roomName)

def deleteRoom(roomName):
    return db.delete(roomName)

def getRoom(roomName):
    return db.get(roomName).items[0]

def joinRoom(roomName, user):
    room = db.get(roomName).items[0]
    newUsers = room["users"]
    userNb = room["userNb"] + 1
    newUsers.append({"username": user, "time": None})
    return db.update(updates={"users": newUsers, "userNb": userNb}, key=roomName)