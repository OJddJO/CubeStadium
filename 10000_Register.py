import streamlit as st
import streamlit_authenticator as sa
import _auth

title = "Register"
st.set_page_config(page_title=title, page_icon="🪪")
st.title(title)

if st.session_state.authentication_status == True:
    st.error("You are already logged in")

if st.session_state.authentication_status == None or st.session_state.authentication_status == False:

    #main
    name = st.text_input("Name", "")
    username = st.text_input("Username", "")
    password = st.text_input("Password", type="password")

    if st.button("Register"):
        if name == "" or username == "" or password == "":
            st.error("Please fill all the fields")
        else:
            st.success("Registered !")
            _auth.insertUser(name, username, password)
            st.session_state.authenticator.login("Login", "main")