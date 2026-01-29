from fastapi import FastAPI
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langserve import add_routes


load_dotenv()


os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

model = ChatGroq(model="llama-3.1-8b-instant", groq_api_key=os.getenv("GROQ_API_KEY"))

generic_prompt = "You are a helpful assistant that translates English to {language}."

prompt = ChatPromptTemplate.from_messages([
    ("system", generic_prompt),
    ("user", "{input}")
])

parser = StrOutputParser()

chain = prompt | model | parser

app = FastAPI(title="Simple LLM with LCEL and Groq API",
              version="0.1.0",
              description="An example FastAPI app using Langchain Execution Chains with Groq API.")

add_routes(app, 
           chain, 
           path="/translate")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
