import streamlit as st
import streamlit.components.v1 as components
from time import sleep, time
from getScrambles import getScramble

title = "PVP"
st.set_page_config(page_title=title, page_icon="⚔️")
st.title(title)
st.header("Coming soon !")
try:
    if st.session_state.authentication_status == None or st.session_state.authentication_status == False:
        st.error("Please login to access this page")

    if st.session_state.authentication_status == True:
        #main
        titleCol, createCol = st.columns(2)
        titleCol.subheader("Room List")
        createCol.button("Create Room")


        st.session_state.authenticator.logout("Logout", "sidebar")
            

except:
    st.error("Please go to home page first")