import os
from pathlib import Path

from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings

BASE_DIR = Path(__file__).resolve().parent

load_dotenv(BASE_DIR / ".env", override=True)

API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("API_KEY is missing from your backend/.env file.")

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001",
    google_api_key=API_KEY
)

vector_store = Chroma(
    collection_name="myCollection",
    embedding_function=embeddings,
    persist_directory=str(BASE_DIR / "chroma_db")
)


def addData(data: list[str]):
    vector_store.add_texts(texts=data)
    print("Data stored successfully!")


def askQuestion(askedQuery: str):
    chunks = vector_store.similarity_search(
        query=askedQuery,
        k=2
    )
    return chunks