import streamlit as st
import streamlit.components.v1 as components
from time import sleep, time
from getScrambles import getScramble
import roomManager

title = "PVP"
st.set_page_config(page_title=title, page_icon="⚔️")
st.title(title)
st.header("Coming soon !")
try:
    if st.session_state.authentication_status == None or st.session_state.authentication_status == False:
        st.error("Please login to access this page")

    if st.session_state.authentication_status == True:
        #main
        def createRoom():
            run = True
            createRoomContainer = mainContainer.container()
            createRoomContainer.subheader("Create Room")
            roomName = createRoomContainer.text_input("Room Name")
            maxUsers = createRoomContainer.number_input("Max Users", min_value=2, max_value=10, value=2)
            roomPassword = createRoomContainer.number_input("Room Password (6 digits max)", min_value=0, max_value=999999)
            scrambleSize = createRoomContainer.selectbox("Scramble Size", ["15", "20", "25", "30"], key="scrambleSizeOption")
            btnCreate, btnCancel = createRoomContainer.columns(2)
            if btnCreate.button("Create"):
                roomManager.createRoom(roomName, st.session_state.username, roomPassword, maxUsers, getScramble(int(scrambleSize)))
                st.success("Created room " + roomName)
                initRoomPage()
            btnState = btnCancel.button("Cancel")
            while run:
                if btnState:
                    run = False


        def refresh():
            get_rooms = roomManager.fetchAllRooms()
            roomListContainer = mainContainer.container()
            roomNames = [name["key"] for name in get_rooms]
            roomAdmin = [admin["admin"] for admin in get_rooms]
            roomMaxUsers = [maxUsers["maxUsers"] for maxUsers in get_rooms]
            roomCurrentUsers = [currentUsers["currentUsers"] for currentUsers in get_rooms]
            roomPassword = [password["password"] for password in get_rooms]
            roomStatus = [status["status"] for status in get_rooms]
            #create expander for each room
            for name in roomNames:
                tmp = roomListContainer.expander(name)
                tmp.subheader("Admin: " + roomAdmin[roomNames.index(name)])
                tmp.subheader("Max Users: " + str(roomMaxUsers[roomNames.index(name)]))
                tmp.subheader("Current Users: " + str(roomCurrentUsers[roomNames.index(name)]))
                tmp.subheader("Status: " + roomStatus[roomNames.index(name)])
                if tmp.button("Join"):
                    joinRoom(name, roomPassword[roomNames.index(name)])


        def joinRoom(name, password):
            run = True
            joinRoomContainer = mainContainer.container()
            joinRoomContainer.subheader("Join Room")
            joinRoomContainer.subheader(name)
            inputPassword = joinRoomContainer.number_input("Room Password", min_value=0, max_value=999999)
            
            btnJoin, btnCancel = joinRoomContainer.columns(2)
            if btnJoin.button("Join"):
                if inputPassword == password:
                    room = roomManager.getRoom(name)
                    if room["currentUsers"] < room["maxUsers"]:
                        roomManager.joinRoom(name)
                        joinRoomContainer.success("Joined room " + name)
                        initRoomPage()
                        run = False
                    else:
                        joinRoomContainer.error("Room is full")
                else:
                    joinRoomContainer.error("Wrong password")
            btnState = btnCancel.button("Cancel")
            while run:
                if btnState:
                    run = False


        def initRoomPage():
            pass


        titleCol, refreshCol, createCol = st.columns(3)
        titleCol.subheader("Room List")
        refreshCol.button("Refresh", on_click=refresh)
        createCol.button("Create Room", on_click=createRoom)

        mainContainer = st.empty()

            


        st.session_state.authenticator.logout("Logout", "sidebar")
            

except:
    st.error("Please go to home page first")