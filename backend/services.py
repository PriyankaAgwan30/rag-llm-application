# from google import genai
# from dotenv import load_dotenv
# import os

# from database import askQuestion
# from langchain_core.prompts import ChatPromptTemplate

# load_dotenv()
# s
# API_KEY = os.getenv("API_KEY")

# client = genai.Client(api_key=API_KEY)


# def create_prompt(question: str) -> str:

#     chunks = askQuestion(question)

#     context = ""

#     for doc in chunks:
#         context += doc.page_content + "\n\n"
        
#     prompt_template = ChatPromptTemplate.from_template("""
#         You are a helpful AI assistant.

#         Answer the user's question using only the
#         information provided in the context.

#         If the answer is not available in the context,
#         respond with:
#         "I don't know based on the provided information."

#         Context:
#         {context}

#         Question:
#         {question}

#         Answer:
#     """)

#     formatted_prompt = prompt_template.invoke({
#         "context": context,
#         "question": question
#     })

#     return formatted_prompt.to_string()


# def findResponse(question: str) -> str:

#     final_prompt = create_prompt(question)

#     response = client.models.generate_content(
#         model="gemini-3.8-flash",
#         contents=final_prompt
#     )

#     return response.text






# def create_prompt(question: str) -> str:
#     print("1. Searching documents...", flush=True)

#     chunks = askQuestion(question)

#     print(f"2. Retrieved {len(chunks)} chunks.", flush=True)

#     context = "\n\n".join(doc.page_content for doc in chunks)

#     return f"""
# Answer the question using only the context below.
# If the answer is unavailable, say:
# "I don't know based on the provided information."

# Context:
# {context}

# Question:
# {question}
# """


# def findResponse(question: str) -> str:
#     final_prompt = create_prompt(question)

#     print("3. Sending request to Gemini...", flush=True)

#     try:
#         response = client.models.generate_content(
#             model="gemini-2.5-flash",
#             contents=final_prompt
#         )
#     except Exception as error:
#         print(f"Gemini error: {error}", flush=True)
#         raise

#     print("4. Gemini response received.", flush=True)

#     return response.text or "No answer was generated."










from google import genai
from database import API_KEY, askQuestion

client = genai.Client(api_key=API_KEY)


def create_prompt(question: str) -> str:
    print("1. Searching documents...", flush=True)

    chunks = askQuestion(question)

    print(f"2. Retrieved {len(chunks)} chunks.", flush=True)

    context = "\n\n".join(doc.page_content for doc in chunks)

    return f"""
Answer the question using only the provided context.
If the answer is unavailable, say:
"I don't know based on the provided information."

Context:
{context}

Question:
{question}
"""


def findResponse(question: str) -> str:
    final_prompt = create_prompt(question)

    print("3. Sending request to Gemini...", flush=True)

    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=final_prompt
        )
    except Exception as error:
        print(f"Gemini error: {error}", flush=True)
        raise

    print("4. Gemini response received.", flush=True)

    return response.text or "No answer was generated."