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
        st.session_state.authenticator.logout("Logout", "sidebar")

        #main
        optionsExpander = st.expander("Scramble Options")
        scrambleSizeOption = optionsExpander.selectbox("Scramble size", ["15", "20", "25", "30"], key="scrambleSizeOption")

        scrambleContainer = st.empty()

        if optionsExpander.button("Re-Scramble"):
            st.session_state.scramble = getScramble(int(scrambleSizeOption))
            scrambleContainer.subheader()
        
        # timer

        timerContainer = st.empty()
        try:
            timerContainer.subheader("{:.2f}".format(st.session_state.timer))
        except:
            st.session_state.scramble = getScramble()
            st.session_state.timer = 0.00
            st.session_state.timerStarted = False
            scrambleContainer.subheader(st.session_state.scramble)
            timerContainer.subheader("{:.2f}".format(st.session_state.timer))

        async def timerFunc():
            buttonState = button.button("Stop")
            scrambleContainer.subheader(st.session_state.scramble)
            st.session_state.timer = 0.00
            while st.session_state.timerStarted:
                st.session_state.timer += 0.01
                timerContainer.subheader("{:.2f}".format(st.session_state.timer))
                await asyncio.sleep(0.01)
                if buttonState:
                    st.session_state.timerStarted = False
                    st.session_state.scramble = getScramble(int(scrambleSizeOption))
                    scrambleContainer.subheader(st.session_state.scramble)
                    break

        button = st.empty()
        if button.button("Start"):
            if st.session_state.timerStarted == False:
                st.session_state.timerStarted = True
                asyncio.run(timerFunc())
            

except Exception as e:
    st.error("Please go to home page first")
    st.error(e)