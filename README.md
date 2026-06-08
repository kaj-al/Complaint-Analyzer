# HybridRAG Complaint Analyzer

A Streamlit powered retrieval augmented generation (RAG) application that analyzes customer complaints using hybrid retrieval.

## What it does

- Loads complaint examples from `Datasetprojpowerbi.csv`
- Builds a hybrid retrieval system using:
  - FAISS dense embeddings (`sentence-transformers/all-MiniLM-L6-v2`)
  - BM25 sparse retrieval
- Sends retrieved context and user complaint to an OpenAIcompatible model via OpenRouter
- Returns structured JSON output with:
  - `category`
  - `severity`
  - `action`

## Files

- `app.py` - Streamlit app UI 
- `pipeline.py` - RAG orchestration logic and structured LLM output handling
- `ingest.py` - Dataset ingestion, embedding generation, and hybrid retriever implementation
- `prompts.py` - Prompt template 
- `Datasetprojpowerbi.csv` - Source complaint dataset used for retrieval
- `requirements.txt` - Python dependencies
- `store/` - Local FAISS index store directory

## Requirements

- Python 3.8+ (recommended Python 3.11+)
- `OPENAI_API_KEY` set in a `.env` file or environment
- Internet access for the OpenRouter/OpenAI API

## Setup

1. Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Create a `.env` file in the repository root with your API key:

```dotenv
OPENAI_API_KEY=your_api_key_here
```

## Run the app

Start Streamlit application:

```powershell
streamlit run app.py
```

## How it works

1. `app.py` collects complaint text from user.
2. `pipeline.py` calls `ingest.hybrid(query)` to retrieve relevant documents.
3. `ingest.py` performs hybrid retrieval using FAISS embeddings and BM25.
4. Retrieved text is combined into prompt defined in `prompts.py`.
5. model returns structured JSON with complaint classification and recommended action.




