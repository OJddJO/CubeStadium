import streamlit as st
from getScrambles import getScramble
from streamlit_elements import elements, event
from time import sleep
from keyboard import on_press_key

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


        with elements("callbaks_hotkey"):
            def spacePressed():
                global timerStarted
                if timerStarted == False:
                    timerStarted = True
            
            event("space", spacePressed)

            while timerStarted == True:
                timer += 0.01
                timerContainer.subheader(timer.__round__(2))
                sleep(0.01)
                if on_press_key("space"):
                    timerStarted = False



except:
    st.error("Please go to home page first")