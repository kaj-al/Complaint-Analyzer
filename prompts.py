from langchain_core.prompts import PromptTemplate


prompt = PromptTemplate(
    input_variables=["context","query"],
    template="""
You are an AI complaint classifier.
Complaint:{query}
Retrieved context:{context}
JSON Format:{{
    "category": "string",
    "severity": "string",
    "action": "string"
}}
Output JSON Only.
"""
)

