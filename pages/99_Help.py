import streamlit as st

st.set_page_config(page_title="Help", page_icon="❓")
st.title("Help")
st.sidebar.markdown("**Made with ❤️ by** [***OJddJO***](https://github.com/OJddJO/)")

auth = st.expander("Authentication")
auth.subheader("I can't register or login")
auth.caption("To register, go to the register page using the sidebar")
auth.caption("- If there is an error, check if you are already logged in")
auth.caption("- If you are not logged in, check if you have filled all the fields")
auth.caption("- If you have filled all the fields, check if your username is already taken")
auth.caption("- Else try to stop your adblocker")

timer = st.expander("Timer")
timer.subheader("I can't start/stop the timer")
timer.caption("To start the timer, click on the start/stop button")
timer.caption("If you're using the spacebar, try again after re-entering")
timer.caption("the timer page (just click on the timer page in the sidebar so you don't have to reload the page)")

