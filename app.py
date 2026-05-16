import streamlit as st 
from pipeline import rag

query = st.text_area("Enter complaint")
if st.button("Analyze"):
    response = rag(query)
    st.json(response)


