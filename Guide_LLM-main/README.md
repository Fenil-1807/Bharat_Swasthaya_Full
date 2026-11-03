# BharatSwasthya AI Guide LLM Service 🌿

FastAPI microservice for the **BharatSwasthya AI** website guide chatbot powered by Google Gemini and LangChain.

---

## 🚀 Quick Start Guide

### 1. Install Dependencies
All requirements are listed in `requirements.txt`.
```bash
pip install -r requirements.txt
```

### 2. Configure Environment Variables
Open the `.env` file in the root folder and add your **Google Gemini API Key**:
```env
GEMINI_API_KEY=AIzaSy...your_gemini_api_key_here
MODEL_NAME=gemini-2.5-flash
HOST=0.0.0.0
PORT=8000
```
> 💡 *Need a Gemini API key?* Get one for free from [Google AI Studio](https://aistudio.google.com/app/apikey).

### 3. Start the Server
Run the project with a single command:
```bash
python run.py
```
*Or using uvicorn directly:*
```bash
uvicorn llm.main:app --reload
```

---

## 📡 API Documentation & Endpoints

Once the server is running, visit:
- **Interactive Swagger Docs:** [http://localhost:8000/docs](http://localhost:8000/docs)
- **Alternative ReDoc:** [http://localhost:8000/redoc](http://localhost:8000/redoc)
- **Health Check:** `GET http://localhost:8000/health`
- **Guide Chatbot:** `POST http://localhost:8000/guide`

---

## 🧪 Testing the API

### Example `POST /guide` Request (cURL):
```bash
curl -X POST "http://localhost:8000/guide" \
     -H "Content-Type: application/json" \
     -d '{
       "message": "How do I check Dengue cases in my district?",
       "chat_history": []
     }'
```

### Example `POST /guide` Request with Conversation History:
```json
{
  "message": "Where is the emergency 108 button located?",
  "chat_history": [
    {
      "role": "user",
      "content": "Hi, what is BharatSwasthya AI?"
    },
    {
      "role": "assistant",
      "content": "BharatSwasthya AI is India's National Epidemiological Outbreak Intelligence & Digital Health Platform..."
    }
  ]
}
```

### Example Response:
```json
{
  "success": true,
  "response": "To find the Emergency 108 button:\n1. Look at the top navigation bar available on all pages.\n2. Click the red button with the phone icon labeled \"Emergency 108\"."
}
```

### Run Python Test Script:
```bash
python test_api.py
```

---

## 📂 Project Structure

```
guideLLM/
├── .env                # Environment variables (API keys, ports)
├── .env.example        # Sample environment configuration template
├── .gitignore          # Git ignore rules
├── requirements.txt    # Project Python dependencies
├── run.py              # Root launcher script
├── test_api.py         # Test script for API verification
└── llm/
    ├── __init__.py
    ├── llm.py          # Gemini LangChain integration & website system prompt
    ├── main.py         # FastAPI application with CORS & routes
    └── requirements.txt
```
