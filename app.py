import os
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_openai import ChatOpenAI

from langgraph.graph import StateGraph, END

import streamlit as st

load_dotenv()

st.title("LangGraph Multi-Agent RAG Chatbot")

uploaded_file = st.file_uploader("Upload PDF", type="pdf")

if uploaded_file:

    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    loader = PyPDFLoader("temp.pdf")
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(docs)

    embeddings = OpenAIEmbeddings()

    vectordb = Chroma.from_documents(
        chunks,
        embeddings
    )

    retriever = vectordb.as_retriever()

    llm = ChatOpenAI(model="gpt-4o-mini")


    class AgentState(dict):
        pass


    def retrieve(state):

        query = state["query"]

        docs = retriever.get_relevant_documents(query)

        return {"docs": docs}


    def reason(state):

        context = "\n".join(
            [doc.page_content for doc in state["docs"]]
        )

        reasoning_prompt = f"""
        Analyze context carefully:

        {context}

        Prepare reasoning for answering:
        {state["query"]}
        """

        response = llm.invoke(reasoning_prompt)

        return {"reasoning": response.content}


    def generate_answer(state):

        final_prompt = f"""
        Use reasoning below:

        {state["reasoning"]}

        Answer clearly:
        {state["query"]}
        """

        response = llm.invoke(final_prompt)

        return {"answer": response.content}


    graph = StateGraph(AgentState)

    graph.add_node("retrieve", retrieve)
    graph.add_node("reason", reason)
    graph.add_node("generate", generate_answer)

    graph.set_entry_point("retrieve")

    graph.add_edge("retrieve", "reason")
    graph.add_edge("reason", "generate")

    graph.add_edge("generate", END)

    app_graph = graph.compile()


    question = st.text_input("Ask question")

    if question:

        result = app_graph.invoke(
            {"query": question}
        )

        st.write(result["answer"])