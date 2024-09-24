import sys, os
import streamlit as st
from langchain_community.vectorstores import FAISS
import pandas as pd
from utils.retriever import SelfQueryRetriever
from langchain_core.messages import AIMessage, HumanMessage
from langchain_community.vectorstores.faiss import DistanceStrategy
from langchain_community.embeddings import HuggingFaceEmbeddings
from utils.llm_agent import ChatBot
import utils.chatbot_verbosity as chatbot_verbosity
from utils.helper import upload_file, check_openai_api_key
import time

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))
GPT_MODEL = "gpt-4o-mini"

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
welcome_message = """
  #### Introduction 🚀

  The system is a RAG pipeline designed to assist hiring managers in searching for the most suitable candidates out of thousands of resumes more effectively. ⚡

  The idea is to use a similarity retriever to identify the most suitable applicants with job descriptions.
  This data is then augmented into an LLM generator for downstream tasks such as analysis, summarization, and decision-making. 

  #### Getting started 🛠️

  1. To set up, please add your OpenAI's API key. 🔑 
  2. Upload a CSV of Resumes with columns "ID" and "Resume". 📄
  3. Type in a job description query. 💬
"""

st.set_page_config(page_title="AI Powered Resume Screening")
st.title("AI Powered Resume Screening")

if "chat_history" not in st.session_state:
  st.session_state.chat_history = [AIMessage(content=welcome_message)]

if "embedding_model" not in st.session_state:
  st.session_state.embedding_model = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL, model_kwargs={"device": "cpu"})

if "resume_list" not in st.session_state:
  st.session_state.resume_list = []

def clear_message():
  st.session_state.resume_list = []
  st.session_state.chat_history = [AIMessage(content=welcome_message)]



user_query = st.chat_input("Type your message here...")

with st.sidebar:
  st.markdown("# Control Panel")

  st.text_input("OpenAI's API Key", type="password", key="api_key")
  st.file_uploader("Upload resumes", type=["csv"], key="uploaded_file", on_change=upload_file)
  st.button("Clear conversation", on_click=clear_message)


for message in st.session_state.chat_history:
  if isinstance(message, AIMessage):
    with st.chat_message("AI"):
      st.write(message.content)
  elif isinstance(message, HumanMessage):
    with st.chat_message("Human"):
      st.write(message.content)
  else:
    with st.chat_message("AI"):
      message[0].render(*message[1:])


if not st.session_state.api_key:
  st.info("Please add your OpenAI API key to continue. Learn more about [API keys](https://platform.openai.com/api-keys).")
  st.stop()

if not check_openai_api_key(st.session_state.api_key):
  st.error("The API key is incorrect. Please set a valid OpenAI API key to continue. Learn more about [API keys](https://platform.openai.com/api-keys).")
  st.stop()

if st.session_state.uploaded_file == None:
  st.error("Please upload your resumes to continue.")
  st.stop()


retriever = st.session_state.rag_pipeline

llm = ChatBot(
  api_key=st.session_state.api_key,
  model=GPT_MODEL,
)

if user_query is not None and user_query != "":
  with st.chat_message("Human"):
    st.markdown(user_query)
    st.session_state.chat_history.append(HumanMessage(content=user_query))

  with st.chat_message("AI"):
    start = time.time()
    with st.spinner("Generating answers..."):
      document_list = retriever.retrieve_docs(user_query, llm, "Generic RAG")
      query_type = retriever.meta_data["query_type"]
      st.session_state.resume_list = document_list
      stream_message = llm.generate_message_stream(user_query, document_list, [], query_type)
    end = time.time()

    response = st.write_stream(stream_message)
    
    retriever_message = chatbot_verbosity
    retriever_message.render(document_list, retriever.meta_data, end-start)

    st.session_state.chat_history.append(AIMessage(content=response))
    st.session_state.chat_history.append((retriever_message, document_list, retriever.meta_data, end-start))