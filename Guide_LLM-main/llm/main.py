import os
from pathlib import Path
from typing import Any, Dict, List, Optional
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

# Discover and load .env from root or local directory
for env_path in [
    Path(__file__).resolve().parent.parent / ".env",
    Path(__file__).resolve().parent / ".env",
    Path.cwd() / ".env",
]:
    if env_path.exists():
        load_dotenv(dotenv_path=env_path)
        break
else:
    load_dotenv()

try:
    from .llm import guide_llm
except (ImportError, ValueError):
    from llm import guide_llm


app = FastAPI(
    title="BharatSwasthya AI Guide API",
    description="Website navigation guide chatbot API for BharatSwasthya AI",
    version="1.0.0",
)

# Enable CORS for cross-origin frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class GuideRequest(BaseModel):
    message: str = Field(..., description="User's question or message regarding the website")
    chat_history: Optional[List[Dict[str, Any]]] = Field(
        default=[],
        description="Prior conversation history in [{'role': 'user'|'assistant', 'content': '...'}] format"
    )


@app.get("/")
async def root():
    return {
        "status": "online",
        "service": "BharatSwasthya AI Guide API",
        "version": "1.0.0",
        "docs": "/docs",
        "health": "/health",
        "guide_endpoint": "POST /guide"
    }


@app.get("/health")
async def health():
    return {
        "status": "ok",
        "service": "BharatSwasthya AI Guide",
    }


@app.post("/guide")
async def guide(request: GuideRequest):
    try:
        response = guide_llm(
            user_message=request.message,
            chat_history=request.chat_history,
        )

        return {
            "success": True,
            "response": response,
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Guide LLM Error: {str(e)}")


if __name__ == "__main__":
    import uvicorn

    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", 8000))
    print(f"🚀 Starting BharatSwasthya AI Guide API on http://{host}:{port}")
    uvicorn.run(app, host=host, port=port)
