import streamlit as st
from PIL import Image
import extension.userData

title = "Stats"
icon = Image.open("icon.png")
st.set_page_config(page_title=title, page_icon=icon)
st.title(title)
st.sidebar.markdown("**Made with ❤️ by** [***OJddJO***](https://github.com/OJddJO/)")

try:
    if st.session_state.authentication_status == None or st.session_state.authentication_status == False:
        st.error("Please login to access this page")

    if st.session_state.authentication_status == True:
        #sidebar
        st.session_state.authenticator.logout("Logout", "sidebar")

        #main
        st.button("Refresh")

        def saveData():
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
            st.experimental_rerun()

        #data
        pb = st.session_state.userDatas[st.session_state.userIndex]["pb"]
        ao5 = st.session_state.userDatas[st.session_state.userIndex]["ao5"]
        ao12 = st.session_state.userDatas[st.session_state.userIndex]["ao12"]
        scrambles = st.session_state.userDatas[st.session_state.userIndex]["scrambles"]
        times = st.session_state.userDatas[st.session_state.userIndex]["times"]
        list_ao5 = st.session_state.userDatas[st.session_state.userIndex]["list_ao5"]
        list_ao12 = st.session_state.userDatas[st.session_state.userIndex]["list_ao12"]

        col1, col2, col3, = st.columns(3)

        col1.metric("Personnal Best:", pb)
        col2.metric("Best average of 5:", ao5)
        col3.metric("Best average of 12:", ao12)

        st.caption("Times (in seconds) :")
        st.area_chart({"Times": times})

        #times
        timesExpander = st.expander("All times")
        if times is not None:
            timesExpander.caption("Green = Better than your ao12, Red = Worse than your ao12, Yellow = Equal to your ao12, Blue = No ao12 yet")
            for element in times:
                if ao12 is not None:
                    if element < ao12:
                        color = ":green"
                    elif element > ao12:
                        color = ":red"
                    else:
                        color = ":yellow"
                else:
                    color = ":blue"
                t, btnDel = timesExpander.columns(2)
                t.markdown(f"{color}[**{element}**]: {scrambles[times.index(element)]}")
                if btnDel.button("Delete", key=f"del{element}-{scrambles[times.index(element)]}"):
                    scrambles.remove(scrambles[times.index(element)])
                    st.session_state.userDatas[st.session_state.userIndex]["scrambles"] = scrambles
                    times.remove(element)
                    st.session_state.userDatas[st.session_state.userIndex]["times"] = times
                    saveData()
        else:
            timesExpander.caption("No times yet")

        #ao5
        ao5Expander = st.expander("All ao5")
        if list_ao5 is not None:
            i = 0
            for element in list_ao5:
                ao5Col, btnDel = ao5Expander.columns(2)
                ao5Col.markdown(element)
                if btnDel.button("Delete", key=f"del{element}-{i}"):
                    list_ao5.remove(element)
                    st.session_state.userDatas[st.session_state.userIndex]["list_ao5"] = list_ao5
                    if ao5 == element:
                        st.session_state.userDatas[st.session_state.userIndex]["ao5"] = min(list_ao5)
                    saveData()
                i += 1
        else:
            ao5Expander.caption("No ao5 yet")

        #ao12
        ao12Expander = st.expander("All ao12")
        if list_ao12 is not None:
            i = 0
            for element in list_ao12:
                ao12Col, btnDel = ao12Expander.columns(2)
                ao12Col.markdown(element)
                if btnDel.button("Delete", key=f"del{element}-{i}"):
                    list_ao12.remove(element)
                    st.session_state.userDatas[st.session_state.userIndex]["list_ao12"] = list_ao12
                    if ao12 == element:
                        st.session_state.userDatas[st.session_state.userIndex]["ao12"] = min(list_ao12)
                    saveData()
                i += 1
        else:
            ao12Expander.caption("No ao12 yet")


except Exception as e:
    st.error("Please go to home page first")
    st.error(e)
