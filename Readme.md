🇮🇳 BHARAT SWASTHYA AI 🚀
Revolutionizing Healthcare Accessibility & Proactive Public Health Intelligence
Explore Features • Architecture Breakdown • Quick Start

🌟 Overview
Bharat Swasthya AI is a cutting-edge, full-stack healthcare platform engineered to bridge the gap between citizens and critical medical infrastructure in India. Powered by state-of-the-art generative AI and real-time backend synchronization, the platform shifts healthcare from reactive treatment to proactive intelligence—offering live hospital bed tracking, automated voice calling agents, multilingual chat assistants, and intelligent predictive health monitoring.

💎 Core Features & Architecture
1. 📞 AI Calling Agent (Voice-First Outreach)
Twilio & AI4Bharat Integration: Enables seamless, natural language voice communication to reach out to citizens, conduct automated health surveys, and relay critical medical advisories.

Multilingual Capabilities: Built to bridge linguistic divides, allowing rural and urban populations to interact effortlessly via voice.

2. ⚡ Proactive LLM Engine
Predictive Health Alerts: Monitors regional health trends and environmental vectors to proactively alert users and administrative bodies regarding potential viral outbreaks or localized disease spikes.

Automated Risk Assessment: Analyzes user inputs and environmental data to trigger early warnings before symptoms escalate.

3. 🧠 Guide LLM & Interactive Chatbot
Intelligent Triage & Navigation: Acts as an empathetic virtual health guide, helping patients navigate symptoms, understand hospital workflows, and find appropriate care tiers.

Context-Aware Conversations: Remembers session states and medical queries to offer precise, safe, and structured guidance.

4. 🏥 Live Hospital Bed Tracking & Resource Explorer
Real-Time Availability: Dynamically tracks bed capacity, ICU units, and oxygen supplies across localized networks.

Interactive Location Dashboards: Seamlessly filter resources by region, hospital tier, and specific emergency needs.

5. 🌐 Comprehensive Web Application & Role Portals
Public Citizen Portal: Clean, accessible interface for booking, searching resources, and interacting with AI tools.

Dedicated Stakeholder Portals: Specialized dashboards for Doctors, Hospital Administrators, Health Assistants, and System Admins to manage patient flows, advisories, and system stats.

🛠️ Technology Stack
Frontend: React.js, Vite, Tailwind CSS, Lucide Icons, Markdown Renderer

Backend: Node.js, Express.js, MongoDB (Mongoose)

AI & Voice Services: Google Gemini API, Twilio Voice API, AI4Bharat Speech Models

Deployment & Config: Vercel-ready configurations, dotenv environment management

📁 Project Structure
Plaintext
Bharat_Swasthaya/
├── BS-AI_website-main/          # Core Web Application Repository
│   ├── client/                  # React Frontend (Tailwind, Dashboards, Modals)
│   └── server/                  # Node.js/Express Backend (Controllers, Models, Routes)
└── BharatSwasthya-AI-main/      # Core AI Service & Health Modules
🚀 Getting Started
Prerequisites
Node.js (v18+ recommended)

MongoDB database instance

API Keys: Gemini API Key, Twilio Account SID & Auth Token

Installation & Setup
Clone the repository / Extract files

Configure Backend Environment:
Navigate to the server directory and create a .env file based on .env.example:

Code snippet
PORT=5000
MONGO_URI=your_mongodb_connection_string
GEMINI_API_KEY=your_google_gemini_api_key
TWILIO_ACCOUNT_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
Install Dependencies & Run Backend:

Bash
cd BS-AI_website-main/server
npm install
npm run dev
Install Dependencies & Run Frontend:

Bash
cd ../client
npm install
npm run dev
🛡️ License & Acknowledgments
Built with passion for transforming healthcare accessibility and intelligence across India.