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

# LLM settup
# prompt
prompt = """
    You are a helpful AI assistant. Your job is to analyze the provided research paper data, to generate insights. Provide:

    1. A summary of the paper.
    2. Insights from the academic paper.
    3. Identify key references.

    Input variables:
    - {paper_data}
    """
# prompt template
prompt_template = ChatPromptTemplate([('system',prompt)])
# chain
chain = prompt_template | llm | parser

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
            # Get the paper insights
            with st.spinner("Analyzing the paper..."):
                paper_data = search.invoke(paper_url)            
                paper_insights = chain.invoke({'paper_data': paper_data})

if paper_insights:
    st.markdown("### Paper Insights")
    st.markdown(paper_insights)