#Import packages
import streamlit as st
from datetime import datetime
#Write title and text
st.title("Guru's first Streamlit App")
st.write("Hello World")
#Gather current Date time
st.write("Current date and time:", datetime.now().strftime("%Y-%m-%d %H:%M: %S"))

#Create button
if st.button("Click Me"):
    st.write("You clicke the button!")