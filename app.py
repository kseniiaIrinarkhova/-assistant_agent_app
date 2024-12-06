# import libs
import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.tools import TavilySearchResults

# Page Config
st.set_page_config(page_title="AI Writing Tool")

# Model and Agent Tools
llm = ChatGroq(api_key=st.secrets['GROQ_API_KEY'])
parser = StrOutputParser()
search = TavilySearchResults(max_results=2)

# Page title
st.title('Assistant Agent')
st.markdown("Assistant Agent Powered by Groq.")
st.markdown("### Help researchers gather insights from academic papers, extract summaries, and identify key references.")