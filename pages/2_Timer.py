import streamlit as st
from getScrambles import getScramble

title = "Timer"
st.set_page_config(page_title=title, page_icon="⏱️")
st.title(title)

if st.session_state.authentication_status == None or st.session_state.authentication_status == False:
    st.error("Please login to access this page")

if st.session_state.authentication_status == True:
    st.session_state.authenticator.logout("Logout", "sidebar")

    #main
    try:
        scrambleContainer = st.empty()
        scrambleContainer.subheader(getScramble(st.session_state.scrambleSizeOption))
    except:
        scrambleContainer.subheader(getScramble())

    scrableSizeOption, rescrambleCol = st.columns(2)
    st.session_state.scrambleSizeOption = scrableSizeOption.selectbox("Scramble size", ["15", "20", "25", "30"], key="scrambleSizeOption")

    if rescrambleCol.button("Rescramble"):
        scrambleContainer.subheader(getScramble(st.session_state.scrambleSizeOption))