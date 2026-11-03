from fastapi import FastAPI
from pydantic import BaseModel
from langchain_core.messages import HumanMessage
from fastapi import HTTPException

from graph import workflow
from utils import extract_text


app = FastAPI(
    title="BharatSwasthya AI"
)

class ChatRequest(BaseModel):
    mongo_id: str
    query: str

@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "BharatSwasthya AI",
        "telephony": "Exotel VoiceBot",
    }

@app.post("/chat")
def chat(request: ChatRequest):

    try:
        result = workflow.invoke(
                {
                    "messages": [
                        HumanMessage(
                            content=request.query
                        )
                    ]
                },
                config={
                    "configurable": {
                        "thread_id": request.mongo_id
                    }
                }
            )
        
        response = extract_text(result["messages"][-1].content)
        
        return {
            "response": response
        }
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail="Service is unavailable. Please try again."
        )