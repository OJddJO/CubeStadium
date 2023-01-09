import streamlit as st
from getScrambles import getScramble
import asyncio
from time import sleep

title = "Timer"
st.set_page_config(page_title=title, page_icon="⏱️")
st.title(title)

try:
    if st.session_state.authentication_status == None or st.session_state.authentication_status == False:
        st.error("Please login to access this page")

    if st.session_state.authentication_status == True:
        #main
        scrambleExpander = st.expander("Scramble Options")
        scrambleSizeOption = scrambleExpander.selectbox("Scramble size", ["15", "20", "25", "30"], key="scrambleSizeOption")

        scrambleContainer = st.empty()

        if scrambleExpander.button("Re-Scramble"):
            st.session_state.scramble = getScramble(int(scrambleSizeOption))
            scrambleContainer.subheader(st.session_state.scramble)

        # timer
        timerContainer = st.empty()
        st.session_state.timerStarted = False
        try:
            scrambleContainer.subheader(st.session_state.scramble)
            timerContainer.title("{:.2f}".format(st.session_state.timer))
        except:
            st.session_state.scramble = getScramble()
            st.session_state.timer = 0.00
            scrambleContainer.subheader(st.session_state.scramble)
            timerContainer.title("{:.2f}".format(st.session_state.timer))


        def timerFunc():
            # init timer with scramble and reset timer
            buttonState = startStop.button("Stop", on_click=stopTimer)
            scrambleContainer.subheader(st.session_state.scramble)
            st.session_state.timer = 0.00
            # start timer
            run = True
            while run:
                st.session_state.timer += 0.01
                timerContainer.title("{:.2f}".format(st.session_state.timer))
                # stop button timer
                if buttonState:
                    # stop timer
                    run = False
                sleep(0.01)
        
        def stopTimer():
            st.session_state.timerStarted = False
            st.session_state.scramble = getScramble(int(scrambleSizeOption))
            scrambleContainer.subheader(st.session_state.scramble)
            st.success("Time registered !")

        startStop = st.empty()
        startStop.button("Start", on_click=timerFunc)


        st.session_state.authenticator.logout("Logout", "sidebar")
            

except Exception as e:
    st.error("Please go to home page first")
    st.error(e)