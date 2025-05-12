import streamlit as st
from the_haiku_poet import haiku_spitter

st.title("Welcome to Haiku Spitter 3000")

# Creates a session state entry that contains all chat messages.
# This is needed because the page is rerendered for every change, so we need to store and rerdisplay previous chat messages.
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "ai", "content": "Gimme a topic, and I shall spit a haiku to you!"}]

for message in st.session_state.messages:
    # use of with block to write text inside of the chat message container
    with st.chat_message(message["role"]):
        st.write(message["content"])

# this is a chat-box style input for the user
user_input = st.chat_input("What's in your mind...")

# when we get user input
if user_input:
    # display the user message as a message (text bubble)
    with st.chat_message("human"):
        st.write(user_input)
    # store message for later rerender
    st.session_state.messages.append({"role": "human", "content": user_input})

    with st.chat_message("ai"):
        response = haiku_spitter(user_input) 
        st.write(response)
    st.session_state.messages.append({"role": "ai", "content": response})
