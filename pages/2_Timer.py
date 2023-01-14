import streamlit as st
import streamlit.components.v1 as components
from extension.getScrambles import getScramble
from extension.cubeModel import Cube
from time import sleep, time
from PIL import Image

title = "Timer"
icon = Image.open("icon.png")
st.set_page_config(page_title=title, page_icon=icon)
st.title(title)
st.sidebar.markdown("**Made with ❤️ by** [***OJddJO***](https://github.com/OJddJO/)")
"""
try:"""
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
        #spacebar trigger button
        components.html(
            """
            <script>
            const doc = window.parent.document;
            buttons = Array.from(doc.querySelectorAll('button[kind=secondary]'));
            const stopButton = buttons.find(el => el.innerText === 'Stop');
            doc.addEventListener('keydown', function(e) {
                switch (e.keyCode) {
                    case 32:
                        stopButton.click();
                        break;
                }
            });
            </script>
            """,
        width=0,
        height=0,
        )
        scrambleContainer.subheader(st.session_state.scramble)
        st.session_state.timer = 0.00
        # start timer
        run = True
        t1 = time()
        while run:
            timerContainer.title("{:.2f}".format(st.session_state.timer))
            t2 = time()
            st.session_state.timer = t2 - t1
            # stop button timer
            if buttonState:
                # stop timer
                run = False
            sleep(0.01)
    
    def stopTimer():
        st.session_state.scramble = getScramble(int(scrambleSizeOption))
        scrambleContainer.subheader(st.session_state.scramble)
        st.success("Time not registered !")

    startStop = st.empty()
    startStop.button("Start", on_click=timerFunc)

    #spacebar trigger button
    components.html(
        """
        <script>
        const doc = window.parent.document;
        buttons = Array.from(doc.querySelectorAll('button[kind=secondary]'));
        const startButton = buttons.find(el => el.innerText === 'Start');
        doc.addEventListener('keydown', function(e) {
            switch (e.keyCode) {
                case 32:
                    startButton.click();
                    break;
            }
        });
        </script>
        """,
        height=0,
        width=0,
    )

    cube = Cube()
    cubeModel = cube.drawCube(st.session_state.scramble)
    st.image(cubeModel)

    st.info("You can use the spacebar to start/stop the timer")


    st.session_state.authenticator.logout("Logout", "sidebar")
            
"""
except Exception as e:
    st.error("Please go to home page first")
    st.error(e)"""