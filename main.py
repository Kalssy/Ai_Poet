import os
import openai
from langchain_openai import ChatOpenAI
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

chat_model = ChatOpenAI(temperature=0, model="gpt-3.5-turbo", openai_api_key=openai.api_key)

st.title("인공지능 시인")
subject = st.text_input("시의 주제를 입력해주세요.")
st.write("시의 주제 : " + subject)

if st.button("시 작성"):
    with st.spinner("시 작성중 ..."):
        response = chat_model(messages=[{"role": "user", "content": f"{subject}에 대한 시를 써줘"}])
        st.write(response.content)
