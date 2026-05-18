import streamlit as st 
from pipeline import rag

st.title("Complaint Analyzer")

st.markdown("""
<style>

.main {
    background-color: #0E1117;
    color: white;
}

.stTextArea textarea {
    border-radius: 12px;
    border: 1px solid #444;
    background-color: white;
    color: black;
    font-size: 16px;
}

.stButton button {
    width: 100%;
    border-radius: 12px;
    height: 50px;
    font-size: 18px;
    font-weight: bold;
    background-color: #7C3AED;
    color: white;
    border: none;
}

.stButton button:hover {
    background-color: #6D28D9;
}

.card {
    padding: 20px;
    border-radius: 15px;
    background-color: white;
    border: 1px solid #333;
    margin-bottom: 15px;
}

.small-title {
    color: #A1A1AA;
    font-size: 14px;
}

.big-text {
    font-size: 24px;
    font-weight: bold;
    color: white;
}

.footer {
    text-align: center;
    color: gray;
    margin-top: 50px;
}

</style>
""", unsafe_allow_html=True)

query = st.text_area("Enter complaint",height=150,placeholder="Describe your issue")
if st.button("Analyze", use_container_width=True):
    with st.spinner("Analyzing"):
        response = rag(query)
        # st.json(response)

        st.subheader("Result")
        col1,col2 = st.columns(2)
        with col1:
            category = response["category"]
            st.markdown(f"""
        <div class="card">
        <div class="small-title>CATEGORY</div>
            <div class="big-text>{category}</div>
        </div>""",unsafe_allow_html=True)
            
        with col2:
            severity = response["severity"]
            st.markdown(f"""
        <div class="card">
        <div class="small-title>SEVERITY</div>
            <div class="big-text>{severity}</div>
        </div>""",unsafe_allow_html=True)   
            
        st.markdown("### Suggested Action")
        st.success(response["action"])
