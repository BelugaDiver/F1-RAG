from fastapi import FastAPI
from rag import rag

app = FastAPI()

@app.get("/")
async def root(question: str) -> dict:
    response = rag(question)

    return {
        "response": response
    }
