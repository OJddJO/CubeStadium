import streamlit as st
import streamlit_authenticator as sa
import _auth

title = "Register"
st.set_page_config(page_title=title, page_icon="🗒️")
st.title(title)


try:
    if st.session_state.authentication_status == True:
        st.error("You are already logged in")
        st.session_state.authenticator.logout("Logout", "sidebar")

    if st.session_state.authentication_status == None or st.session_state.authentication_status == False:
        # main
        regContainer = st.container()
        name = regContainer.text_input("Name", "")
        username = regContainer.text_input("Username", "")
        password = regContainer.text_input("Password", type="password")

        # get all usernames to test if it already exists
        users = _auth.fetchAllUsers()
        usernames = [user["key"] for user in users]

        if regContainer.button("Register"):
            if name == "" or username == "" or password == "":
                st.error("Please fill all the fields")
            elif username in usernames:
                st.error("Username already exists")
            else:
                st.success("Registered !")
                st.info("You can now login at the home page")
                _auth.insertUser(name, username, password)
except:
        #main
        regContainer = st.container()
        name = regContainer.text_input("Name", "")
        username = regContainer.text_input("Username", "")
        password = regContainer.text_input("Password", type="password")

        # get all usernames to test if it already exists
        users = _auth.fetchAllUsers()
        usernames = [user["key"] for user in users]

        if regContainer.button("Register"):
            if name == "" or username == "" or password == "":
                st.error("Please fill all the fields")
            elif username in usernames:
                st.error("Username already exists")
            else:
                st.success("Registered !")
                st.info("You can now login at the home page")
                _auth.insertUser(name, username, password)