import streamlit as st
import streamlit.components.v1 as components
from extension.getScrambles import getScramble
from extension.cubeModel import Cube
from time import sleep, time
from PIL import Image
import extension.userData
from random import randint

title = "Timer"
icon = Image.open("icon.png")
st.set_page_config(page_title=title, page_icon=icon)
st.title(title)
st.sidebar.markdown("**Made with ❤️ by** [***OJddJO***](https://github.com/OJddJO/)")

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
        except Exception as e:
            st.session_state.scramble = getScramble()
            st.session_state.timer = 0.00
            scrambleContainer.subheader(st.session_state.scramble)
            timerContainer.title("{:.2f}".format(st.session_state.timer))


        def timerFunc():
            # init timer with scramble and reset timer
            buttonState = startStop.button("Stop", on_click=stopTimer)
            st.session_state.run = True
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
                st.session_state.timer = round(t2 - t1, 2)
                # stop button timer
                if buttonState:
                    # stop timer
                    run = False
                sleep(0.01)
            # wait until st.session_state.run == False
            while st.session_state.run:
                pass

        def stopTimer():
            st.session_state.scramble = getScramble(int(scrambleSizeOption))
            scrambleContainer.subheader(st.session_state.scramble)
            #save time and scramble
            #retrieve user data
            pb = st.session_state.userDatas[st.session_state.userIndex]["pb"]
            scrambles = st.session_state.userDatas[st.session_state.userIndex]["scrambles"]
            times = st.session_state.userDatas[st.session_state.userIndex]["times"]
            list_ao5 = st.session_state.userDatas[st.session_state.userIndex]["list_ao5"]
            list_ao12 = st.session_state.userDatas[st.session_state.userIndex]["list_ao12"]

            # update user data
            # add time and scramble
            scrambles.append(st.session_state.scramble)
            st.session_state.userDatas[st.session_state.userIndex]["scrambles"] = scrambles
            times.append(st.session_state.timer)
            st.session_state.userDatas[st.session_state.userIndex]["times"] = times
            # update ao5
            if pb == None or st.session_state.timer < pb:
                st.session_state.userDatas[st.session_state.userIndex]["pb"] = st.session_state.timer
            try:
                tmp_ao5 = times[-5:]
                tmp_ao5.append(st.session_state.timer)
                tmp_ao5 = tmp_ao5[0:5]
                if len(tmp_ao5) == 5:
                    tmp_ao5.remove(min(tmp_ao5))
                    tmp_ao5.remove(max(tmp_ao5))
                    tmp_ao5 = round(sum(tmp_ao5)/len(tmp_ao5), 2)
                    list_ao5.append(tmp_ao5)
                    st.session_state.userDatas[st.session_state.userIndex]["list_ao5"] = list_ao5
                    try:
                        if tmp_ao5 < st.session_state.userDatas[st.session_state.userIndex]["ao5"]:
                            st.session_state.userDatas[st.session_state.userIndex]["ao5"] = tmp_ao5
                    except:
                        st.session_state.userDatas[st.session_state.userIndex]["ao5"] = tmp_ao5
            except:
                st.session_state.userDatas[st.session_state.userIndex]["list_ao5"] = []

            # update ao12
            try:
                tmp_ao12 = times[-12:]
                tmp_ao12.append(st.session_state.timer)
                tmp_ao12 = tmp_ao12[0:12]
                if len(tmp_ao12) == 12:
                    tmp_ao12.remove(min(tmp_ao12))
                    tmp_ao12.remove(max(tmp_ao12))
                    tmp_ao12 = round(sum(tmp_ao12)/len(tmp_ao12), 2)
                    list_ao12.append(tmp_ao12)
                    st.session_state.userDatas[st.session_state.userIndex]["list_ao12"] = list_ao12
                    try:
                        if tmp_ao12 < st.session_state.userDatas[st.session_state.userIndex]["ao12"]:
                            st.session_state.userDatas[st.session_state.userIndex]["ao12"] = tmp_ao12
                    except:
                        st.session_state.userDatas[st.session_state.userIndex]["ao12"] = tmp_ao12
            except:
                st.session_state.userDatas[st.session_state.userIndex]["list_ao12"] = []

            # save user data in db
            data = {
                "pb": st.session_state.userDatas[st.session_state.userIndex]["pb"],
                "ao5": st.session_state.userDatas[st.session_state.userIndex]["ao5"],
                "ao12": st.session_state.userDatas[st.session_state.userIndex]["ao12"],
                "scrambles": st.session_state.userDatas[st.session_state.userIndex]["scrambles"],
                "times": st.session_state.userDatas[st.session_state.userIndex]["times"],
                "list_ao5": st.session_state.userDatas[st.session_state.userIndex]["list_ao5"],
                "list_ao12": st.session_state.userDatas[st.session_state.userIndex]["list_ao12"],
            }
            extension.userData.updateData(st.session_state.username, {"data": data})

            st.session_state.run = False
            st.success("Time registered !")


        #spacebar trigger button
        def triggerButton():
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

        startStop = st.empty()
        btnStart = startStop.button("Start", on_click=timerFunc)
        if btnStart:
            btnStart = False
            btnStart = startStop.button("Start", on_click=timerFunc, key=randint(0, 1000000000))
            triggerButton()

        triggerButton()

        cube = Cube()
        cubeModel = cube.drawCube(st.session_state.scramble)
        st.image(cubeModel)

        st.info("You can use the spacebar to start/stop the timer")
        st.info("Use the R key to be able to use the spacebar if it doesn't work")

        st.session_state.authenticator.logout("Logout", "sidebar")


except Exception as e:
    st.error("Please go to home page first")
    st.error(e)
