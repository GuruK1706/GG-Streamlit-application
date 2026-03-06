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

#Write header and subheader
st.header("Basic Streamlit Header")
st.subheader("Widgets")

#Create number slider widget
number = st.slider("Pick a number", 0, 100, 25)
st.write("You picked:", number)

#Create text input widget
text = st.text_input("Enter some text")
st.write("You typed:", text)

#Create multiselect widget
options = st.multiselect("Choose your pizza toppings", ["Chesse","Mushrooms","Onions"])
st.write("Toppings ", options)


