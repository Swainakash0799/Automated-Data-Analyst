import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()


def create_llm():

    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError(
            "GROQ_API_KEY not found in .env file"
        )

    return ChatGroq(
        model="qwen/qwen3.8-27b",
        api_key=api_key,
        temperature=0
    )


def analyze_data(llm, question, eda_result):

    prompt = f"""
You are an expert data analyst.

Use only the provided EDA results.

User Question:
{question}

EDA Results:
{eda_result}

Do not invent numbers.
Give a clear and concise answer.
"""

    response = llm.invoke(prompt)

    return response.content