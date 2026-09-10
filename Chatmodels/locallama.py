from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

import streamlit as st  
import os
from dotenv import load_dotenv


load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"


promt=ChatPromptTemplate.from_messages(
    [
        ('system', "You are a helpful assistant. Please response to the queries"),
        ('user','Qestion: {question}')
    ]

)

# stramlit app


st.title("Langchain Chatbot")
input_text = st.text_input("Enter your question here:")


# Ollama LLm
llm = Ollama(model="llama2")
output_parser = StrOutputParser()   
chain=promt | llm | output_parser

if input_text:
    response = chain.invoke({"question": input_text})
    st.write("Response:", response)