import streamlit as st
from extension.getScrambles import getScramble
import extension.roomManager
from PIL import Image
from time import sleep, time
from extension.cubeModel import Cube

title = "PVP"
icon = Image.open("icon.png")
st.set_page_config(page_title=title, page_icon=icon)
st.title(title)
st.info("Still in development ... 🛠️")
st.header("Coming soon !")
st.sidebar.markdown("**Made with ❤️ by** [***OJddJO***](https://github.com/OJddJO/)")

try:
    if st.session_state.authentication_status == None or st.session_state.authentication_status == False:
        st.error("Please login to access this page")

    if st.session_state.authentication_status == True:
        try:
            if st.session_state.inRoom == True:
                pass
        except:
            st.session_state.inRoom = False

        #main
        if st.session_state.inRoom == False:
            #join room
            def refresh():
                get_rooms = extension.roomManager.fetchAllRooms()
                roomListContainer = mainContainer.container()
                get_rooms = [room for room in get_rooms if room["data"]["status"] == "waiting"]
                roomNames = [name["key"] for name in get_rooms]
                roomAdmin = [admin["data"]["admin"] for admin in get_rooms]
                roomMaxUsers = [maxUsers["data"]["maxUsers"] for maxUsers in get_rooms]
                roomCurrentUsers = [currentUsers["data"]["userNb"] for currentUsers in get_rooms]
                roomPassword = [password["data"]["password"] for password in get_rooms]
                roomStatus = [status["data"]["status"] for status in get_rooms]
                #create expander for each room
                for name in roomNames:
                    tmp = roomListContainer.expander(name)
                    tmp.caption("Admin: " + roomAdmin[roomNames.index(name)])
                    tmp.caption("Max Users: " + str(roomMaxUsers[roomNames.index(name)]))
                    tmp.caption("Current Users: " + str(roomCurrentUsers[roomNames.index(name)]))
                    tmp.caption("Status: " + roomStatus[roomNames.index(name)])


            def joinRoom(name, inputPassword):
                password = extension.roomManager.getRoom(name)["data"]["password"]
                if inputPassword == password:
                    room = extension.roomManager.getRoom(name)
                    if room["data"]["userNb"] < room["data"]["maxUsers"]:
                        extension.roomManager.joinRoom(name, st.session_state.username)
                        st.session_state.inRoom = True
                        st.session_state.roomData = extension.roomManager.getRoom(name)
                        joinRoomContainer.success("Joined room " + name)
                    else:
                        joinRoomContainer.error("Room is full")
                else:
                    joinRoomContainer.error("Wrong password")


            #create room
            createRoomContainer = st.expander("Create Room")
            createRoomName = createRoomContainer.text_input("Room Name")
            maxUsers = createRoomContainer.number_input("Max Users", min_value=2, max_value=10, value=2)
            createRoomPassword = createRoomContainer.number_input("Room Password (6 digits max)", min_value=0, max_value=999999)
            scrambleSize = createRoomContainer.selectbox("Scramble Size", ["15", "20", "25", "30"], key="scrambleSizeOption")
            def createRoom(roomName, username, roomPassword, maxUsers, scrambleSize):
                extension.roomManager.createRoom(roomName, username, roomPassword, maxUsers, getScramble(int(scrambleSize)))
                createRoomContainer.success("Created room " + roomName)
                joinRoom(roomName, roomPassword)
            createRoomContainer.button("Create", on_click=createRoom, args=(createRoomName, st.session_state.username, createRoomPassword, maxUsers, scrambleSize))

            #join room
            joinRoomContainer = st.expander("Join Room")
            roomName = joinRoomContainer.text_input("Room Name", key="joinRoomName")
            roomPassword = joinRoomContainer.number_input("Room Password", min_value=0, max_value=999999, key="joinRoomPassword")
            joinRoomContainer.button("Join", on_click=joinRoom, args=(roomName, roomPassword))

            #room list
            titleCol, refreshCol = st.columns(2)
            titleCol.subheader("Room List")
            refreshCol.button("Refresh", on_click=refresh)

            mainContainer = st.empty()

            refresh() # refresh room list


            st.session_state.authenticator.logout("Logout", "sidebar")
        
        elif st.session_state.inRoom == True:
            #room page
            while st.session_state.roomData["data"]["status"] == "waiting":
                playerListContainer = st.expander("Player List")
                playerListContainer.caption("Admin: " + st.session_state.roomData["data"]["admin"])
                for player in st.session_state.roomData["data"]["users"]:
                    playerListContainer.caption(player, key=player)
                
                #if admin then show start button
                if st.session_state.username == st.session_state.roomData["data"]["admin"]:
                    def startRoom():
                        st.session_state.roomData["data"]["status"] = "started"
                        extension.roomManager.updateRoom(st.session_state.roomData["key"], st.session_state.roomData["data"])
                        st.success("Room started")
                    startRoomContainer = st.expander("Admin")
                    startRoomContainer.button("Start", on_click=startRoom)
                
                #if not admin then show waiting message
                else:
                    st.info("Waiting for admin to start the room ...")
                
                #check if room is started
                def checkRoomStatus():
                    st.session_state.roomData = extension.roomManager.getRoom(st.session_state.roomData["key"])
                
                checkRoomStatus()
                sleep(5)

            st.session_state.time = 0
            st.session_state.scramble = st.session_state.roomData["data"]["scramble"]
            
            while st.session_state.roomData["data"]["status"] == "started":
                scrambleContainer = st.empty()


except Exception as e:
    st.error("Please go to home page first")
