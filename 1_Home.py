import streamlit as st
import streamlit_authenticator as sa
import extension._auth
from PIL import Image


title = "Cube Stadium"
icon = Image.open("icon.png")
st.set_page_config(page_title=title, page_icon=icon)
st.title(title)
st.info("Still in development ... 🛠️")
st.sidebar.markdown("**Made with ❤️ by** [***OJddJO***](https://github.com/OJddJO/)")

# authentication
get_users = extension._auth.fetchAllUsers()
usernames = [user["key"] for user in get_users]
names = [user["name"] for user in get_users]
hashedPasswords = [user["password"] for user in get_users]
userDatas = [user["data"] for user in get_users]

st.session_state.authenticator = sa.Authenticate(names, usernames, hashedPasswords, "cubestadium", "secret")

name, authenticationStatus, username = st.session_state.authenticator.login("Login", "main")

if authenticationStatus == False:
    st.error("Username/password is incorrect")

if authenticationStatus == None:
    st.warning("Please enter your username and password")

if authenticationStatus == True:
    st.success("Logged in as {}".format(name))

    #sidebar
    st.session_state.authenticator.logout("Logout", "sidebar")

    #main

    #get user data
    st.session_state.userIndex = usernames.index(username)

    st.session_state.pb = userDatas[st.session_state.userIndex]["pb"]
    st.session_state.ao5 = userDatas[st.session_state.userIndex]["ao5"]
    st.session_state.ao12 = userDatas[st.session_state.userIndex]["ao12"]
    st.session_state.scrambles = userDatas[st.session_state.userIndex]["scrambles"]
    st.session_state.times = userDatas[st.session_state.userIndex]["times"]
    st.session_state.list_ao5 = userDatas[st.session_state.userIndex]["list_ao5"]
    st.session_state.list_ao12 = userDatas[st.session_state.userIndex]["list_ao12"]

    try:
        delta_pb = st.session_state.pb - st.session_state.times[-1]
    except:
        delta_pb = None
    try:
        delta_ao5 = st.session_state.ao5 - st.session_state.list_ao5[-1]
    except:
        delta_ao5 = None
    try:
        delta_ao12 = st.session_state.ao12 - st.session_state.list_ao12[-1]
    except:
        delta_ao12 = None

    st.subheader("👋 Welcome to Cube Stadium !")
    col1, col2, col3, = st.columns(3)
    col1.metric("Personnal Best:", st.session_state.pb, delta_pb, delta_color="inverse")
    col2.metric("Average of 5:", st.session_state.ao5, delta_ao5, delta_color="inverse")
    col3.metric("Average of 12:", st.session_state.ao5, delta_ao12, delta_color="inverse")

