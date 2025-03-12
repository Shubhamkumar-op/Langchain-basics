import streamlit as st 
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama

import os
from dotenv import load_dotenv

load_dotenv()

os.environ['LANGCHAIN_API_KEY'] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]="O&A chatbot with Ollama"

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a Rude assistant, Please response to the user queies"),
        ("user","Question:{question}")
    ]
)

def generate_response(question,llm,temperature,max_tokens):
    llm=Ollama(model=llm)
    output_parser=StrOutputParser()
    chain=prompt|llm|output_parser
    answer=chain.invoke({'question':question})
    return answer

st.title("Enhanced Q&A chatbot with Ollama")

# st.slidebar.title("Settings")
# api_key=st.sidebar.text_input("Enter your Langchain API key",type="password")

llm=st.sidebar.selectbox("Select Open Source model",["mistral"])

temperature = st.sidebar.slider("Temperature",min_value=0.0,max_value=1.0,value=0.7)
max_tokens = st.sidebar.slider("Max tokens",min_value=50,max_value=2048,value=150)

st.write("Go ahead and ask question")
user_input=st.text_input("You:")

if user_input:
    response=generate_response(user_input,llm,temperature,max_tokens)
    st.write(response)
else:
    st.write("Please enter a question")