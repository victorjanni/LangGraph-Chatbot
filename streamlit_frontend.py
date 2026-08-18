from langgraph_backend import chatbot
import streamlit as st
from langchain_core.messages import HumanMessage

# st.session_state -> dict ->
CONFIG = {'configurable': {'thread_id': 'thread-1'}}

if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

# loading the chat history
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])

# taking user input
user_input = st.chat_input('Type here ...')

if user_input:
    # frist adding message to message history
    st.session_state['message_history'].append({'role': 'user', 'content': user_input})
    with st.chat_message('user'):
        st.text(user_input)
    response = chatbot.invoke({'messages': [HumanMessage(content=user_input)]}, config=CONFIG)

    ai_message = response['messages'][-1].content

    st.session_state['message_history'].append({'role':'assistant', 'content':ai_message})
    with st.chat_message('assistant'):
        st.text(ai_message)