import streamlit as st
import streamlit_authenticator as sa
import _auth


title = "Cube Stadium"
st.set_page_config(page_title=title, page_icon="👋")
st.title(title)

# authentication
get_users = _auth.fetchAllUsers()
usernames = [user["key"] for user in get_users]
names = [user["name"] for user in get_users]
hashed_passwords = [user["password"] for user in get_users]

st.session_state.authenticator = sa.Authenticate(names, usernames, hashed_passwords,
    "sales_dashboard", "secret", cookie_expiry_days=30)

st.session_state.name, st.session_state.authentication_status, st.session_state.username = st.session_state.authenticator.login("Login", "main")

if st.session_state.authentication_status == False:
    st.error("Username/password is incorrect")

if st.session_state.authentication_status == None:
    st.warning("Please enter your username and password")

if st.session_state.authentication_status == True:
    st.success("Logged in as {}".format(st.session_state.name))

    #sidebar
    st.session_state.authenticator.logout("Logout", "sidebar")

    #main
    pb = 0.00; delta_pb = 0.00
    ao5 = 0.00; delta_ao5 = 0.00
    ao12 = 0.00; delta_ao12 = 0.00

    st.subheader("👋 Welcome to Cube Stadium !")
    col1, col2, col3, = st.columns(3)
    col1.metric("Personnal Best:", pb, delta_pb, delta_color="inverse")
    col2.metric("Average of 5:", ao5, delta_ao5, delta_color="inverse")
    col3.metric("Average of 12:", ao5, delta_ao12, delta_color="inverse")
