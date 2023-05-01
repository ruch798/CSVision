import openai
import streamlit as st
from langchain.agents import create_csv_agent
from langchain.llms import OpenAI
from typing import TextIO

openai.api_key = st.secrets["OPENAI_API_KEY"]

def get_answer(file: TextIO, query: str) -> str:
    agent = create_csv_agent(OpenAI(temperature=0), file, verbose=False)
    answer = agent.run(query)
    return answer
