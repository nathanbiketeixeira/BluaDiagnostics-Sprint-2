import streamlit as st
from src.graph.langgraph_flow import run_graph

st.title("BluaDiagnostics")

user_input = st.text_input("Digite seus sintomas")

if st.button("Enviar"):
    response = run_graph(user_input)
    st.json(response)
