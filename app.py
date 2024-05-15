# Q&A Chatbot

from langchain.llms import OpenAI

#from dotenv import load_dotenv

#load_dotenv() # take all the environment variables from .env

import streamlit as st
import os
## Function to load OpenAI model and get responses

def get_openai_response(question):
    #llm = OpenAI(openai_api_key=os.getenv("OPEN_API_KEY"),model_name="gpt-3.5-turbo",temperature=0.5)
    #llm = OpenAI(model_name="gpt-3.5-turbo",temperature=0.5)
    llm = OpenAI(model="gpt-3.5-turbo",temperature=0.5)
    response=llm(question)
    return response

## initialize the streamlit app

st.set_page_config(page_title="Q&A Demo")

st.header("LangChain Application")


input = st.text_input("Input: ", key=input)
response = get_openai_response(input)


submit = st.button("Ask the Question")

# If ask button is clicked 

if submit:
    st.subheader("The Response is")
    st.write(response)

