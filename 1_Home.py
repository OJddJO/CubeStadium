import streamlit as st
import streamlit_authenticator as sa
import _auth


title = "Cube Stadium"
st.set_page_config(page_title=title, page_icon="👋")
st.title(title)
st.info("Still in development ... 🛠️")
st.sidebar.markdown("**Made with ❤️ by** ***OJddJO***")

# authentication
get_users = _auth.fetchAllUsers()
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
    userIndex = usernames.index(username)

    pb = userDatas[userIndex]["pb"]
    ao5 = userDatas[userIndex]["ao5"]
    ao12 = userDatas[userIndex]["ao12"]
    scrambles = userDatas[userIndex]["scrambles"]
    times = userDatas[userIndex]["times"]
    list_ao5 = userDatas[userIndex]["list_ao5"]
    list_ao12 = userDatas[userIndex]["list_ao12"]

    try:
        delta_pb = pb - times[-1]
    except:
        delta_pb = None
    try:
        delta_ao5 = ao5 - list_ao5[-1]
    except:
        delta_ao5 = None
    try:
        delta_ao12 = ao12 - list_ao12[-1]
    except:
        delta_ao12 = None

    st.subheader("👋 Welcome to Cube Stadium !")
    col1, col2, col3, = st.columns(3)
    col1.metric("Personnal Best:", pb, delta_pb, delta_color="inverse")
    col2.metric("Average of 5:", ao5, delta_ao5, delta_color="inverse")
    col3.metric("Average of 12:", ao5, delta_ao12, delta_color="inverse")
