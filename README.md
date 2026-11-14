🇮🇳 Bharat Swasthya AI

AI-Powered Healthcare Accessibility & Proactive Public Health Intelligence

Explore. Discover. Get Assisted. Stay Healthy.

Bharat Swasthya AI is an AI-powered healthcare platform designed to make healthcare information more accessible, simplify healthcare discovery, and support proactive public health awareness.

The platform brings together healthcare discovery, AI-powered assistance, conversational support, and health intelligence into one unified ecosystem.

---

📌 Table of Contents

- "Overview" (#-overview)
- "Key Features" (#-key-features)
- "Platform Modules" (#-platform-modules)
- "System Architecture" (#-system-architecture)
- "Technology Stack" (#-technology-stack)
- "Project Structure" (#-project-structure)
- "Getting Started" (#-getting-started)
- "Environment Configuration" (#-environment-configuration)
- "Future Scope" (#-future-scope)
- "Contributing" (#-contributing)
- "Disclaimer" (#-disclaimer)

---

🌐 Overview

Accessing reliable healthcare information can be challenging, especially when people struggle to find nearby healthcare facilities, understand available services, or navigate complex healthcare resources.

Bharat Swasthya AI aims to address these challenges through an integrated digital healthcare ecosystem.

The platform focuses on three major pillars:

Pillar| Purpose
🏥 Healthcare Discovery| Simplifies the discovery of hospitals, healthcare facilities, departments, and available resources.
🤖 AI-Powered Assistance| Helps users understand healthcare information through conversational AI.
📊 Proactive Health Intelligence| Supports public health awareness through disease-related insights and geographical intelligence.

---

🚀 Key Features

1. 🏥 Healthcare Discovery

A healthcare discovery experience that helps users explore healthcare facilities and relevant services.

- Search for hospitals and healthcare facilities.
- Explore departments and available services.
- View facility-related information.
- Access bed availability information where supported.
- Make healthcare discovery more accessible through a unified interface.

2. 🤖 Guide LLM — AI Healthcare Assistant

An AI-powered conversational assistant designed to help users navigate healthcare-related information.

- Understands natural-language questions.
- Provides conversational healthcare guidance.
- Helps users explore healthcare services.
- Simplifies access to relevant healthcare information.
- Supports a more accessible interaction experience.

3. 📊 Proactive LLM — Health Intelligence

A proactive health intelligence component focused on disease awareness and public health insights.

- Disease-related information and reports.
- Health trend analysis.
- Geographical health insights.
- Potential outbreak awareness.
- Data-driven public health intelligence.

4. 💬 AI Chatbot

A conversational interface that allows users to interact with the platform and access assistance through natural-language queries.

5. 📞 AI Calling Agent

A voice-based assistance concept intended to make healthcare information more accessible to people who may have difficulty using conventional digital interfaces.

Potential capabilities include:

- Voice-based interaction.
- Conversational assistance.
- Healthcare information access.
- Support for users with limited digital literacy.

Availability of individual voice and telephony integrations depends on the configured services.

---

🧩 Platform Modules

The project is organized into multiple components, each responsible for a specific part of the healthcare ecosystem.

Module| Responsibility
"BS-AI_website-main"| Main web application
"BharatSwasthya-AI-main/health"| Healthcare-related functionality
"Guide_LLM-main"| AI-powered healthcare guidance
"ProactiveLLM-main"| Proactive health intelligence
"chatbot-main"| Conversational chatbot
"BharatCode.txt"| Supporting project documentation

---

🏗️ System Architecture

The following diagram represents the logical organization of the platform and its major components.

flowchart TD
    A[User] --> B[Bharat Swasthya AI Web Platform]

    B --> C[Healthcare Discovery]
    B --> D[Guide LLM]
    B --> E[Proactive LLM]
    B --> F[AI Chatbot]
    B --> G[AI Calling Agent]

    C --> H[Healthcare Information]
    D --> I[AI-Powered Guidance]
    E --> J[Health Intelligence]
    F --> I
    G --> I

    H --> K[Unified Healthcare Experience]
    I --> K
    J --> K

This is a high-level conceptual architecture. Actual integrations and communication between modules depend on their individual implementations.

---

🛠️ Technology Stack

The project brings together web development, backend services, databases, and AI technologies.

Category| Technologies
Frontend| React.js, JavaScript, HTML, CSS
Backend| Node.js, Express.js
Database| MongoDB
AI & LLM| Generative AI, Large Language Models
AI Integration| Gemini API (where configured)
Voice Integration| Twilio (where configured)
Development Tools| Git, GitHub, VS Code

The technologies listed reflect the project's intended or identified technology stack. Individual modules may use different dependencies or configurations.

---

📂 Project Structure

Bharat_Swasthaya_Full/
│
├── BS-AI_website-main/
│   ├── client/
│   └── server/
│
├── BharatSwasthya-AI-main/
│   └── health/
│
├── Guide_LLM-main/
│
├── ProactiveLLM-main/
│
├── chatbot-main/
│
├── BharatCode.txt
│
└── README.md

The repository contains multiple modules. Each module may have its own dependencies, configuration files, and execution instructions.

---

⚙️ Getting Started

Follow these steps to get the project running locally.

Prerequisites

Make sure you have the following installed:

- "Node.js" (https://nodejs.org/)
- npm
- "Git" (https://git-scm.com/)
- MongoDB, if required by the module you want to run
- API credentials for external services, where applicable

1. Clone the Repository

git clone https://github.com/Fenil-1807/Bharat_Swasthaya_Full.git

2. Navigate to the Project

cd Bharat_Swasthaya_Full

3. Install Dependencies

The project contains multiple modules. Navigate to the relevant module directory and install its dependencies.

For example:

cd BS-AI_website-main/client
npm install

For the backend:

cd ../server
npm install

Repeat the process for other modules that contain their own "package.json" files.

4. Configure Environment Variables

Create the required ".env" files in the relevant module directories.

Refer to each module's configuration and source code to identify the required environment variable names.

5. Run the Application

Check the "scripts" section of the relevant "package.json" file to identify the available commands.

For example, if the module defines a development script:

npm run dev

Run each required service according to its individual setup instructions.

---

🔐 Environment Configuration

Some modules may require external API credentials or service configuration.

Examples include:

- Database connection strings.
- AI model API keys.
- Voice or telephony service credentials.
- Other third-party service configuration.

Important security practices:

- Never commit API keys or passwords.
- Keep credentials inside ".env" files.
- Add ".env" files to ".gitignore".
- Use environment variables instead of hardcoding secrets.
- Do not expose private credentials in frontend code.

---

🔮 Future Scope

Bharat Swasthya AI can be extended with additional capabilities to improve accessibility and public health intelligence.

- 🌍 Multilingual Assistance: Support for more Indian languages.
- 📞 Advanced Voice Assistance: Improved voice-based healthcare interactions.
- 🗺️ Geospatial Health Intelligence: More detailed geographical disease analysis.
- 🏥 Real-Time Healthcare Data: Improved integration with healthcare facilities and live capacity information.
- 🔔 Proactive Notifications: Timely public health alerts and awareness messages.
- 📈 Advanced Analytics: Better disease trend analysis and predictive insights.
- 🏛️ Healthcare Ecosystem Integration: Integration with relevant public healthcare services and digital health initiatives.

---

🤝 Contributing

Contributions, suggestions, and improvements are welcome.

1. Fork the repository.
2. Create a new branch.

git checkout -b feature/your-feature-name

3. Make your changes.
4. Commit your changes.

git commit -m "Add: your feature description"

5. Push your branch.

git push origin feature/your-feature-name

6. Open a Pull Request.

---

⚠️ Disclaimer

Bharat Swasthya AI is a technology project intended to improve access to healthcare-related information and public health awareness.

It is not a substitute for professional medical advice, diagnosis, or treatment. Users should consult qualified healthcare professionals for medical decisions.

Information and availability of services depend on the accuracy, freshness, and integration of the underlying data sources.

---

👨‍💻 Project Repository

GitHub: "Fenil-1807/Bharat_Swasthaya_Full" (https://github.com/Fenil-1807/Bharat_Swasthaya_Full)

## 📄 License

This project is licensed under the MIT License.
See the [LICENSE](LICENSE) file for details.

🇮🇳 Building a More Accessible Healthcare Future

One Platform. Smarter Healthcare. Better Awareness.

