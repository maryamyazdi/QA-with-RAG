import streamlit as st
import os

from src.llm import LLMInterface
from src.utils import load_pdfs
from src.vector_db import Faiss

st.set_page_config(page_title="RAG QA", page_icon="./static/icons8-search-120.png")

st.session_state["vector_store"] = None

st.title("🔎 Search in documents")

st.write("### Upload the files")
user_namespace = st.selectbox(
    "Choose the directory containing your files:",
    options=[os.path.join(os.getcwd(), "src/user_docs")],
    index=None,
    placeholder="Select a path",
)

if user_namespace:
    uploaded_pdfs = load_pdfs(dir=user_namespace)

    with st.spinner(f"Indexing the files"):
        db = Faiss()
        db.add(uploaded_pdfs)
        st.session_state["vector_store"] = db

if st.session_state["vector_store"]:
    st.success(f"{len(uploaded_pdfs)} file(s) indexed!")
st.divider()
st.write("### Enter your query")

col1, col2, col3 = st.columns([0.5, 0.2, 0.2])

with col1:
    query = st.text_input("Query:")

with col2:
    selected_model = st.selectbox(
        "Preferred LLM:",
        options=["Gemma2: 2B", "Phi3 Mini"],
        index=0,
    )

with col3:
    n_results = st.selectbox(
        "No. retrieved results:", options=[n for n in range(1, 8)], index=1
    )


if query and st.session_state["vector_store"]:
    a = st.session_state["vector_store"].query(query=query, n_results=n_results)
    st.write(a, type(a))

    if st.button("Search"):
        with st.spinner("Searching..."):
            search_results = db.query(query)
            llm_interface = LLMInterface()
            response = llm_interface.query(
                retrieved_responses=search_results,
                user_query=query,
                llm_name=selected_model,
            )
        st.write("### Generated Response:\n", response)
