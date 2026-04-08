# LangGraph Multi-Agent RAG Chatbot



A production-style \*\*Multi-Agent Retrieval-Augmented Generation (RAG) chatbot\*\* built using \*\*LangGraph, OpenAI embeddings, and ChromaDB\*\* that enables semantic question answering over uploaded PDF documents.



This project demonstrates agent-based LLM orchestration using a structured pipeline of retrieval, reasoning, and response-generation agents.



---



## Features



\- Multi-agent orchestration using LangGraph

\- Upload and query PDF documents interactively

\- Semantic search using vector embeddings

\- Retriever agent for context extraction

\- Reasoning agent for structured interpretation

\- Answer generation agent using LLM

\- Streamlit-based interactive UI

\- Modular pipeline design suitable for production-style AI workflows



\---



## Tech Stack



\- Python

\- LangGraph

\- LangChain

\- OpenAI API

\- ChromaDB (Vector Database)

\- Streamlit



\---



## Architecture Workflow

User uploads PDF

↓

Document Loader

↓

Text Chunking

↓

Embedding Generation

↓

Vector Storage (ChromaDB)

↓

Retriever Agent

↓

Reasoning Agent

↓

Answer Generator Agent

↓

Final Response to User





\---



## Installation \& Setup



### Step 1: Clone Repository





git clone https://github.com/Pranjalmishr1/langgraph-multiagent-rag-chatbot.git



cd langgraph-multiagent-rag-chatbot





### Step 2: Create Virtual Environment





python -m venv venv

venv\\Scripts\\activate





### Step 3: Install Dependencies





pip install -r requirements.txt





(or install manually if requirements.txt not added yet)





pip install langchain langgraph chromadb streamlit python-dotenv langchain-community langchain-openai langchain-text-splitters pypdf





\---



### Step 4: Add OpenAI API Key



Create `.env` file inside project root:





OPENAI\_API\_KEY=your\_api\_key\_here





\---



### Step 5: Run Application





streamlit run app.py





Then open:





http://localhost:8501





Upload a PDF and start asking questions.



\---



## Example Use Cases



\- Resume understanding assistant

\- Research paper summarizer

\- Study notes QA assistant

\- Policy document analyzer

\- Knowledge-base chatbot



\---



## Future Improvements



\- Multi-document simultaneous querying

\- Conversation memory agent

\- Tool-calling agent integration

\- Local LLM support (Ollama)

