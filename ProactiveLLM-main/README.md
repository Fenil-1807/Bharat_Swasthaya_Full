# Proactive Health Intelligence LLM System

An autonomous, multi-agent proactive intelligence pipeline built with **LangGraph**, **Google Gemini**, and **Tavily Search**. It continuously evaluates local meteorological conditions, hospital epidemiology telemetry, and live real-time web outbreak intelligence to generate proactive clinical and community health advisories.

---

## 4-Node Multi-Agent Architecture

```
                       [ Input: State, District, City ]
                                      │
                                      ▼
             ┌──────────────────────────────────────────────────┐
             │       Node 1: Real-time Weather Telemetry        │
             │   - Open-Meteo Geocoded Meteorological Ingestion │
             │   - Temp, Humidity, Rain, Vector Breeding Risk   │
             └──────────────────────────────────────────────────┘
                                      │
                                      ▼
             ┌──────────────────────────────────────────────────┐
             │      Node 2: Active Viral Outbreak Telemetry     │
             │   - Hospital & Database Epidemiological Records  │
             │   - Dengue, H3N2, Pathogen Severity & Clusters   │
             └──────────────────────────────────────────────────┘
                                      │
                                      ▼
             ┌──────────────────────────────────────────────────┐
             │  Node 3: Climate & Environmental ReAct Agent     │
             │   - ReAct Agent with Google / Tavily Search Tool │
             │   - Natural Climate Anomalies & Climate Change   │
             │   - Extreme Weather Warnings (Floods/Heatwaves)  │
             │   - Air Quality Index (AQI), Smog & Pollution    │
             └──────────────────────────────────────────────────┘
                                      │
                                      ▼
             ┌──────────────────────────────────────────────────┐
             │        Node 4: Proactive LLM Reasoner            │
             │   - Multi-Hazard Synthesis with Google Gemini    │
             │   - Climate-Disease Vulnerability Correlation    │
             │   - Clinical Protocols, Red Flags & Precautions  │
             └──────────────────────────────────────────────────┘
                                      │
                                      ▼
                     [ Structured Proactive Advisory JSON ]
```

---

## Features

- **Node 1 (Weather Telemetry)**: Ingests current conditions and 10-day meteorological forecasts (temperature, humidity, precipitation, standing water stagnation indices).
- **Node 2 (Outbreak Telemetry)**: Queries hospital and public health epidemiological records for confirmed local pathogen clusters and clinical severity.
- **Node 3 (Natural Climate & Environmental Surveillance ReAct Agent)**: Uses an autonomous **ReAct agent with Google/Tavily search** to gather real-time intelligence on **natural climate shifts, climate change impacts, extreme weather events (floods, heatwaves, cyclones), Air Quality Index (AQI) / smog pollution, and environmental hazards**.
- **Node 4 (Multi-Hazard Proactive LLM Reasoner)**: Synthesizes weather forecasts, hospital viral disease telemetry, and live web climate/environmental intelligence to deliver actionable clinical guidance, public precautions, and red-flag danger alerts.
- **FastAPI API Server**:
  - `POST /api/v1/proactive-advisory`
  - `GET /api/v1/proactive-advisory`
  - `GET /health`
  - `GET /docs` (Interactive OpenAPI Swagger documentation)

---

## Project Structure

```
ProactiveLLM/
├── agent/
│   ├── __init__.py
│   ├── tools.py       # Weather, Database & Tavily Search Tool functions
│   ├── nodes.py       # LangGraph Nodes (Weather, DB Disease, ReAct Agent, LLM Reasoner)
│   ├── graph.py       # LangGraph 4-Node StateGraph pipeline builder
│   ├── agent.py       # High-level pipeline execution wrapper
│   ├── main.py        # FastAPI server endpoints
│   └── requirements.txt
├── tests/
│   └── test_pipeline.py  # End-to-end automated pytest suite
├── conftest.py
├── .env.example
├── .env
└── README.md
```

---

## Quickstart & Installation

### 1. Configure Environment Variables
Copy `.env.example` to `.env` and set your API keys:

```bash
# .env
GEMINI_API_KEY=your_gemini_api_key_here
GEMINI_MODEL=gemini-2.5-flash
TAVILY_API_KEY=your_tavily_api_key_here
BACKEND_API_BASE_URL=http://localhost:5000
PORT=8000
HOST=0.0.0.0
```

> **Note**: If `TAVILY_API_KEY` is omitted, the system utilizes intelligent fallback surveillance telemetry to ensure zero pipeline downtime.

### 2. Install Dependencies
```bash
pip install -r agent/requirements.txt
```

### 3. Run the FastAPI Server
```bash
python -m uvicorn agent.main:app --host 0.0.0.0 --port 8000 --reload
```
Or directly:
```bash
python agent/main.py
```

---

## Running Automated Tests

Run the comprehensive pytest suite covering all 4 nodes, ReAct agent execution, Tavily search tool, and FastAPI endpoints:

```bash
pytest -v tests/test_pipeline.py
```

---

## API Documentation

### Proactive Advisory Endpoint (POST)
**Endpoint:** `POST /api/v1/proactive-advisory`  
**Headers:** `Content-Type: application/json`

**Request Body:**
```json
{
  "state": "Maharashtra",
  "district": "Pune",
  "city": "Shivajinagar",
  "language": "Hindi"
}
```

> **Note**: `language` is optional (defaults to `"English"`). Supports any major language, such as Hindi, Marathi, Gujarati, Bengali, Tamil, Telugu, Spanish, French, etc.

**Response Payload:**
```json
{
  "state": "Maharashtra",
  "district": "Pune",
  "city": "Shivajinagar",
  "language": "Hindi",
  "weather_data": {
    "location": "Shivajinagar, Maharashtra",
    "temperature_c": 28.5,
    "humidity_percent": 65,
    "daily_forecast": [...]
  },
  "disease_data": {
    "statusCode": 200,
    "data": {
      "count": 2,
      "data": [
        {
          "diseaseName": "Influenza A (H3N2 Subtype)",
          "totalCases": 12,
          "highestSeverity": "moderate"
        },
        {
          "diseaseName": "Dengue Fever (DENV-2 Strain)",
          "totalCases": 6,
          "highestSeverity": "high"
        }
      ]
    }
  },
  "climate_environment_data": "Live Climate & Environmental Hazard Surveillance for Shivajinagar, Pune, Maharashtra...",
  "llm_output": "सक्रिय जलवायु और जन स्वास्थ्य परामर्श (Shivajinagar, Pune):\n\n1. प्राकृतिक जलवायु और पर्यावरणीय खतरे: तापमान 28.5°C, आर्द्रता 65%...\n2. जलवायु-रोग भेद्यता सहसंबंध: उच्च आर्द्रता के कारण डेंगू मच्छरों का पनपना...\n3. सामुदायिक सावधानियां...\n4. आपातकालीन लक्षण..."
}
```

---

### Proactive Advisory Endpoint (GET)
**Endpoint:** `GET /api/v1/proactive-advisory?state=Maharashtra&district=Pune&city=Shivajinagar&language=Marathi`

Executes the pipeline with query parameters and returns the proactive advisory generated in the requested language.

---


### Health Check Endpoint (GET)
**Endpoint:** `GET /health`

Returns system and node pipeline operational status:
```json
{
  "status": "ok",
  "service": "BharatSwasthya AI - ProactiveLLM",
  "nodes": [
    "Node 1: Weather Telemetry (Open-Meteo)",
    "Node 2: Outbreak Telemetry (Hospital/Viral DB)",
    "Node 3: Natural Climate & Environmental Hazard Surveillance (ReAct Agent + Google Search/Tavily)",
    "Node 4: Multi-Hazard Proactive LLM Synthesis (Gemini Reasoner)"
  ]
}
```
