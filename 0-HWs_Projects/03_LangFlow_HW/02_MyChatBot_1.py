import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
import streamlit as st

load_dotenv()
os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")

llm=ChatGroq(model="qwen-2.5-32b")

st.title("🤖 Chatbot with Streamlit & Groq")

if "messages" not in st.session_state:
    st.session_state.messages=[]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg['content'])

user_input= st.chat_input("Type your message")

if user_input:
    st.session_state.messages.append({"role":"user", "content":user_input})
    
    with st.chat_message("user"):
        st.markdown(user_input)

    response= llm.invoke(user_input).content

    st.session_state.messages.append({"role":"assistant", "content":response})

    with st.chat_message("assistant"):
        st.markdown(response)