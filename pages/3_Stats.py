import streamlit as st
from PIL import Image

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

        timesExpander = st.expander("All times", expanded=True)
        timesExpander.caption("Green = Better than your ao12, Red = Worse than your ao12, Yellow = Equal ao12")
        for element in times:
            if element < ao12:
                color = ":green"
            elif element > ao12:
                color = ":red"
            else:
                color = ":yellow"
            t, btnDel = timesExpander.columns(2)
            t.markdown(f"{color}[**{element}**]: {scrambles[times.index(element)]}")
            if btnDel.button("Delete", key=f"del{element}-{scrambles[times.index(element)]}"):
                times.remove(element)
                scrambles.remove(scrambles[times.index(element)])
                st.experimental_rerun()

        ao5Expander = st.expander("All ao5")
        for element in list_ao5:
            ao5Expander.markdown(element)
        
        ao12Expander = st.expander("All ao12")
        for element in list_ao12:
            ao12Expander.markdown(element)


except Exception as e:
    st.error("Please go to home page first")
