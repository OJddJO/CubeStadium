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
st.session_state.userDatas = [user["data"] for user in get_users]

st.session_state.authenticator = sa.Authenticate(names, usernames, hashedPasswords, "cubestadium", "secret")

name, authenticationStatus, st.session_state.username = st.session_state.authenticator.login("Login", "main")

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
    st.session_state.userIndex = usernames.index(st.session_state.username)

    pb = st.session_state.userDatas[st.session_state.userIndex]["pb"]
    ao5 = st.session_state.userDatas[st.session_state.userIndex]["ao5"]
    ao12 = st.session_state.userDatas[st.session_state.userIndex]["ao12"]
    scrambles = st.session_state.userDatas[st.session_state.userIndex]["scrambles"]
    times = st.session_state.userDatas[st.session_state.userIndex]["times"]
    list_ao5 = st.session_state.userDatas[st.session_state.userIndex]["list_ao5"]
    list_ao12 = st.session_state.userDatas[st.session_state.userIndex]["list_ao12"]

    st.subheader("👋 Welcome to Cube Stadium !")
    col1, col2, col3, = st.columns(3)
    col1.metric("Personnal Best:", pb)
    col2.metric("Average of 5:", ao5)
    col3.metric("Average of 12:", ao12)

