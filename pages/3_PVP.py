import streamlit as st
import streamlit.components.v1 as components
from time import sleep, time
from getScrambles import getScramble
import roomManager

title = "PVP"
st.set_page_config(page_title=title, page_icon="⚔️")
st.title(title)
st.header("Coming soon !")
st.sidebar.markdown("**Made with ❤️ by** [***OJddJO***](https://github.com/OJddJO/)")
try:
    if st.session_state.authentication_status == None or st.session_state.authentication_status == False:
        st.error("Please login to access this page")

    if st.session_state.authentication_status == True:
        #main
            


        def refresh():
            get_rooms = roomManager.fetchAllRooms()
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
                tmp.button("Join", on_click=joinRoom, args=(name, roomPassword[roomNames.index(name)]))


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
                    if room["data"]["currentUsers"] < room["data"]["maxUsers"]:
                        roomManager.joinRoom(name)
                        joinRoomContainer.success("Joined room " + name)
                        initRoomPage()
                        run = False
                    else:
                        joinRoomContainer.error("Room is full")
                else:
                    joinRoomContainer.error("Wrong password")
            btnState = btnCancel.button("Cancel")


        def initRoomPage():
            pass


        titleCol, refreshCol = st.columns(2)
        titleCol.subheader("Room List")
        refreshCol.button("Refresh", on_click=refresh)

        mainContainer = st.empty()

        createRoomContainer = st.expander("Create Room")
        roomName = createRoomContainer.text_input("Room Name")
        maxUsers = createRoomContainer.number_input("Max Users", min_value=2, max_value=10, value=2)
        roomPassword = createRoomContainer.number_input("Room Password (6 digits max)", min_value=0, max_value=999999)
        scrambleSize = createRoomContainer.selectbox("Scramble Size", ["15", "20", "25", "30"], key="scrambleSizeOption")
        def createRoom():
            roomManager.createRoom(roomName, st.session_state.username, roomPassword, maxUsers, getScramble(int(scrambleSize)))
            createRoomContainer.success("Created room " + roomName)
            initRoomPage()
        createRoomContainer.button("Create", on_click=createRoom)

        refresh() # refresh room list


        st.session_state.authenticator.logout("Logout", "sidebar")
            

except Exception as e:
    st.error("Please go to home page first")
    st.error(e)