# Assistant Agent App

Assiatant Agent for analysis of information, provided by URL.
Agent uses LangChain for chaining command, Groq for connection to LLM, and Tavily for url search.


## Project content
- **app.py** - main program
- **requirements.txt** - list of libs
- **.streamlit/secrets.toml.example** - example of sectrets settings

## Installation

1. Copy repository.
2. Create Python Environment (venv) in VS Code. 
3. Register in [Groq.com](https://console.groq.com/) and create an API key
4. Register in [Tavily.com](https://tavily.com/) and create an API key
5. Rename **secrets.toml.example** to **secrets.toml**
6. Save your API keys in **secrets.toml**
7. Install the packages: `pip install -r requiements.txt`
8. Run the app: `streamlit run app.py`
