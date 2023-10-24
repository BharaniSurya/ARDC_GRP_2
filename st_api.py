import streamlit as st
from streamlit_chat import message
import requests

st.set_page_config(
    page_title="Streamlit Chat - Demo",
    page_icon=":robot:"
)

st.header("Streamlit Chat - Demo")

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

def call_api(user_query):
    response = requests.post("http://localhost:5000/generate", json={"query": user_query})
    return response.json()

def get_text():
    input_text = st.text_input("You: ","Hello", key="input")
    return input_text

user_input = get_text()

if user_input:
    output = call_api(user_input)

    st.session_state.past.append(user_input)
    st.session_state.generated.append(output["response"])

if st.session_state['generated']:

    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')





