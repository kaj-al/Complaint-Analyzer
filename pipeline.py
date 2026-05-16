from pydantic.v1 import BaseModel
from ingest import hybrid
from langchain_openai import ChatOpenAI
from prompts import prompt
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
    max_tokens=1600
)

class ComplaintOut(BaseModel):
    category:str
    severity:str
    action:str

def rag(query):
    docs = hybrid(query)
    context = "\n".join([doc.page_content for doc in docs])
    final_prompt = prompt.format(
        context=context,
        query=query
    )
    struct_llm = llm.with_structured_output(ComplaintOut)
    result = struct_llm.invoke(final_prompt)
    return result.dict()
    



