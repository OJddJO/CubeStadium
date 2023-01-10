import streamlit as st
import streamlit.components.v1 as components
from getScrambles import getScramble
from time import sleep, time

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
            t1 = time()
            while run:
                timerContainer.title("{:.2f}".format(st.session_state.timer))
                # stop button timer
                if buttonState:
                    # stop timer
                    run = False
                t2 = time()
                st.session_state.timer = t2 - t1
                sleep(0.01)
        
        def stopTimer():
            st.session_state.scramble = getScramble(int(scrambleSizeOption))
            scrambleContainer.subheader(st.session_state.scramble)
            st.success("Time not registered !")

        startStop = st.empty()
        startStop.button("Start", on_click=timerFunc)

        components.html(
        """
        <script>
        const doc = window.parent.document;
        buttons = Array.from(doc.querySelectorAll('button[kind=secondary]'));
        try {
            const startButton = buttons.find(el => el.innerText === 'Start');
            doc.addEventListener('keydown', function(e) {
                switch (e.keyCode) {
                    case 32:
                        startButton.click();
                        break;
                }
            });
        } catch {
            const stopButton = buttons.find(el => el.innerText === 'Stop');
            doc.addEventListener('keydown', function(e) {
                switch (e.keyCode) {
                    case 32:
                        stopButton.click();
                        break;
                }
            });
        };
        </script>
        """,
            height=0,
            width=0,
        )


        st.session_state.authenticator.logout("Logout", "sidebar")
            

except:
    st.error("Please go to home page first")