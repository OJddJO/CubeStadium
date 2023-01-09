import streamlit as st
from getScrambles import getScramble
from time import sleep

title = "Timer"
st.set_page_config(page_title=title, page_icon="⏱️")
st.title(title)

try:
    if st.session_state.authentication_status == None or st.session_state.authentication_status == False:
        st.error("Please login to access this page")

    if st.session_state.authentication_status == True:
        st.session_state.authenticator.logout("Logout", "sidebar")

        #main
        optionsExpander = st.expander("Scramble Options")
        scrambleSizeOption = optionsExpander.selectbox("Scramble size", ["15", "20", "25", "30"], key="scrambleSizeOption")

        scrambleContainer = st.empty()
        try:
            scrambleContainer.subheader(getScramble(int(scrambleSizeOption)))
        except:
            scrambleContainer.subheader(getScramble())

        if optionsExpander.button("Re-Scramble"):
            scrambleContainer.subheader(getScramble(int(scrambleSizeOption)))
        
        # timer

        timerContainer = st.empty()
        timer = 0.00
        timerStarted = False
        timerContainer.subheader(timer.__round__(2))


except Exception as e:
    st.error("Please go to home page first")
    st.error(e)