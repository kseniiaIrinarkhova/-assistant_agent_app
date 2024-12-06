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

# Data collection
with st.form("paper_research", clear_on_submit=True):
    # Get the URL of the paper
    paper_url = st.text_input("Enter the URL of the paper you want to analyze")
    # Get the research question
    submit_button = st.form_submit_button(label='Analyze')
    paper_insights = ""
    # Check if the form is submitted
    if submit_button:
        if paper_url:
            st.spinner("Analyzing the paper...")
            # Get the paper insights
            paper_data = search.invoke(paper_url)
            print(paper_data)
