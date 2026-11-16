# from fastapi import FastAPI
# from pydantic import BaseModel

# from database import addData

# app = FastAPI(title = "RAG Application")

# #Class to take input document of list 
# class DocumentInput(BaseModel) : 
#     documents : list[str]

# #Class to take input prompt from user of string 
# class ChatInput(BaseModel) :
#     prompt : str

# @app.get("/")
# def home() :
#     return {"message": "Hello! Welcome to RAG Application."}

# #Getting input data
# @app.post("/collection")
# def store_data(documents : DocumentInput) :
#     #Calling fuction, passing input document to perform embedding for converting chunks into vector
#     addData(documents.data)
#     return {"message": "Document stored successfully!"}

# #Function addData
# def addData(data : list) : 
#     #Function of langchain
#     vector_store.addtexts(
#         texts = data
#     )
#     print("Data stored successfully!")

# @app.post("/chat")
# def input_chat(query : ChatInput) :
#     response = findResponse(query.prompt)
#     return {"response" : response}

# # def findResponse(question : str) -> str :
# #     final_prompt = create_prompt(question)

# #     response = client.models.generate_content(
        
# #     )




from fastapi import FastAPI
from pydantic import BaseModel

from database import addData
from services import findResponse

app = FastAPI(title="RAG Application")


class DocumentInput(BaseModel):
    documents: list[str]


class ChatInput(BaseModel):
    prompt: str


@app.get("/")
def home():
    return {"message": "Hello! Welcome to RAG Application."}


@app.post("/collection")
def store_data(documents: DocumentInput):
    addData(documents.documents)
    return {"message": "Documents stored successfully!"}


@app.post("/chat")
def input_chat(query: ChatInput):
    response = findResponse(query.prompt)
    return {"response": response}