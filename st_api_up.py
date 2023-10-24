import streamlit as st
from streamlit_chat import message
import requests

st.set_page_config(
    page_title="Streamlit Chat - Demo",
    page_icon=":robot:"
)

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

def call_api(user_query):
    response = requests.post("http://localhost:5000/generate", json={"query": user_query})
    return response.json()

st.title("Hotline Disaster chatbot")

if 'user_input' not in st.session_state:
    st.session_state.user_input = ""

# Place the chat history above the chat input
st.markdown('<div class="chat-box" id="chat-box" style="order: 1;"></div>', unsafe_allow_html=True)

# Use chat_input for the user's input
user_input = st.chat_input("You:")

if user_input:
    output = call_api(user_input)

    st.session_state.past.append(user_input)
    st.session_state.generated.append(output["response"])

if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])):
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
        message(st.session_state["generated"][i], key=str(i))
