import streamlit as st
import streamlit.components.v1 as components
from time import sleep, time
from getScrambles import getScramble

st.title("PVP")
st.header("Coming soon !")
try:
    if st.session_state.authentication_status == None or st.session_state.authentication_status == False:
        st.error("Please login to access this page")

    if st.session_state.authentication_status == True:
        #main
        titleCol, createCol = st.columns(2)
        


        st.session_state.authenticator.logout("Logout", "sidebar")
            

except:
    st.error("Please go to home page first")