import streamlit as st
from langgraph_backend import chatbot
from langchain_core.messages import HumanMessage, ai_message
import uuid

# ***** utility functions *****

def generate_thread_id():
    thread_id = uuid.uuid4()
    return thread_id

def reset_chat():
    thread_id = generate_thread_id()
    st.session_state['thread_id'] = thread_id
    add_thread(st.session_state['thread_id'])
    st.session_state['message_history'] = []

def add_thread(thread_id):
    if thread_id not in st.session_state['chat_threads']:
        st.session_state['chat_threads'].append(thread_id)

def load_conversion(thread_id):
    state = chatbot.get_state(config={'configurable': {'thread_id': thread_id}})
    # check if messages key exists in state values , return empty list if not 
    return state.values.get('messages', [])

# ***** session setup *****

