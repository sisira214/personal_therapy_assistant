import streamlit as st
import random
import time
import nbimporter
from grokApp import get_response

# Streamed response emulator
def response_generator():
    response = random.choice(
        [
            "Hello there! I am your Personal Therapist:) How can I assist you today?",
            
        ]
    )
    for word in response.split():
        yield word + " "
        time.sleep(0.05)

st.set_page_config(page_title="Personal Therapist", page_icon="🧠")
st.title("🪞 Your Personal AI Therapist")

# Initialize chat history
if "memory" not in st.session_state:
    st.session_state.memory = []
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("How are you feeling today"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    joined_memory = "\n".join(chat for chat in st.session_state.memory)
    chat_template = f"previpus Conversation:\n{joined_memory}\nLatest Query: {prompt}"

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        streamed_text=""

        response = get_response(chat_template)

        for word in response.split():
            streamed_text += word + " "
            response_placeholder.markdown(streamed_text + "")
        response_placeholder.markdown(streamed_text)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": streamed_text})
    st.session_state.memory.append(f"user: {prompt}\nAgent: {streamed_text}")
                                    
    st.session_state.memory = st.session_state.memory[-5:]                                