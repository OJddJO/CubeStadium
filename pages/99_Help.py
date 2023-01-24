import streamlit as st
from PIL import Image

icon = Image.open("icon.png")
st.set_page_config(page_title="Help", page_icon=icon)
st.title("Help")
st.sidebar.markdown("**Made with ❤️ by** [***OJddJO***](https://github.com/OJddJO/)")

auth = st.expander("Authentication")
auth.subheader("I can't register or login")
auth.caption("- To register, go to the register page using the sidebar")
auth.caption("- Make sure you have validated all the fields before clicking on the register button (just click outside the entry before clicking register)")
auth.caption("- If there is an error, check if you are already logged in")
auth.caption("- If you are not logged in, check if you have filled all the fields")
auth.caption("- If you have filled all the fields, check if your username is already taken")
auth.caption("- Else try to stop your adblocker")

timer = st.expander("Timer")
timer.subheader("I can't start/stop the timer")
timer.caption("To start the timer, click on the start/stop button")
timer.caption("If you're using the spacebar, try again after re-entering\nthe timer page (just click on the timer page in the sidebar so you don't have to reload the page)")
timer.caption("Or you can just use the button to start and stop with the spacebar")
timer.subheader("Where is the +2/DNF/Delete button?")
timer.caption("Remember one rule: *+2/DNF doesn't count at home*")
timer.caption("The delete button can be found in the **Stats** page")


