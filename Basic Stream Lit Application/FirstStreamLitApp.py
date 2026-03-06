#Import packages
import streamlit as st
from datetime import datetime
#Write title and text
st.title("Guru's first Streamlit App: Basic UI display, Handle User inoput, Chat Input & Display")
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

#Determine if chat history exists in the session state and initialize if it doesn't

if "chat_history" not in st.session_state:
    st.session_state.chat_history= []
#Create text input widget for user input #Key should be unique
user_msg = st.text_input("You:", key="user_msg_input")
#Create button to append user's message to chat history
if st.button("Send", key="send_button"):
    if user_msg:
        st.session_state.chat_history.append(f"You: {user_msg}")
#Display all messages from chat history
for msg in st.session_state.chat_history:
    st.write(msg)

