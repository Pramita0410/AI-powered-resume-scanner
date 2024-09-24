from streamlit_modal import Modal
import streamlit as st
import os
import sys
import pandas as pd
from utils.ingest_data import ingest
from utils.retriever import SelfQueryRetriever
from langchain_community.vectorstores import FAISS
from langchain_community.vectorstores.faiss import DistanceStrategy
import openai

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))

def upload_file():
  modal = Modal(key="Demo Key", title="File Error", max_width=500)
  try:  
    df_load = pd.read_csv(st.session_state.uploaded_file)
  except Exception as error:
    with modal.container():
      st.markdown("The uploaded file returns the following error message. Please check your csv file again.")
      st.error(error)
  else:
    if "Resume" not in df_load.columns or "ID" not in df_load.columns:
      with modal.container():
        st.error("Please include the following columns in your data: \"Resume\", \"ID\".")
    else:
      with st.toast('Indexing the uploaded data. This may take a while...'):
        st.session_state.df = df_load
        vectordb = ingest(st.session_state.df, "Resume", st.session_state.embedding_model)
        st.session_state.rag_pipeline  = SelfQueryRetriever(vectordb, st.session_state.df)
        st.session_state.retriever = SelfQueryRetriever(vectordb, st.session_state.df)

def check_openai_api_key(api_key: str):
  openai.api_key = api_key
  try:
    openai.models.list()
  except openai.AuthenticationError as e:
    return False
  else:
    return True