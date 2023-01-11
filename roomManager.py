import os
import deta

conn = deta.Deta(os.environ["db_key"])
db = conn.Base("cubestadium_pvpRoom")

def createRoom(roomName, user, password, maxUsers, scramble):
    roomData = {
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
    return db.put({"key": roomName, "data": roomData})

def fetchAllRooms():
    return db.fetch().items

def updateRoom(roomName, updates):
    return db.update(updates=updates, key=roomName)

def leaveRoom(roomName, user):
    room = db.get(roomName).items[0]
    if user == room["data"]["admin"]:
        return db.delete(roomName)
    else:
        newUsers = []
        for u in room["data"]["users"]:
            if u["data"]["username"] != user:
                newUsers.append(u)
        userNb = room["data"]["userNb"] - 1
        update = room["data"]
        update["users"] = newUsers
        update["userNb"] = userNb
        return db.update(updates={"data": update}, key=roomName)

def deleteRoom(roomName):
    return db.delete(roomName)

def getRoom(roomName):
    return db.get(roomName).items[0]

def joinRoom(roomName, user):
    room = db.get(roomName).items[0]
    newUsers = room["data"]["users"]
    userNb = room["data"]["userNb"] + 1
    newUsers.append({"username": user, "time": None})
    update = room["data"]
    update["users"] = newUsers
    update["userNb"] = userNb
    return db.update(updates={"data": update}, key=roomName)