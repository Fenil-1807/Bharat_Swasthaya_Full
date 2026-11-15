# 🇮🇳 BharatSwasthya AI

**An agentic, multilingual healthcare ecosystem for India, reachable through the web and through an ordinary phone call.**

BharatSwasthya AI connects citizens, frontline health workers, doctors, hospitals, and public-health administrators through AI-powered guidance, government scheme intelligence, hospital resource discovery, and proactive disease early-warning advisories.

> Healthcare Accessibility • Agentic AI • Preventive Intelligence

---

## 📌 Overview

Healthcare information, hospital resources, government schemes, and disease surveillance in India often live on separate, disconnected platforms. This creates accessibility barriers, particularly for rural communities and underserved populations.

BharatSwasthya AI brings these services together into one connected, intelligent ecosystem. It links citizens, frontline health workers, doctors, hospitals, and public-health administrators through multilingual AI assistance, voice-based healthcare access, intelligent knowledge retrieval, hospital resource discovery, and proactive disease intelligence.

The platform is built around three principles:

- **🌐 Accessibility:** healthcare information is available through both a website and ordinary phone calls.
- **🧠 Intelligence:** Agentic AI and Retrieval-Augmented Generation (RAG) connect healthcare information and services.
- **🛡️ Prevention:** validated community health reports are combined with environmental intelligence to support early identification of potential regional health risks.

> **Disclaimer:** BharatSwasthya AI supports healthcare awareness and navigation. It does not replace qualified medical professionals.

---

## 🎯 Motivation

India's healthcare ecosystem faces several interconnected challenges:

- Healthcare information is fragmented across different platforms and systems.
- It is difficult to find appropriate medical facilities and know what resources they have available.
- Awareness and understanding of government healthcare schemes is limited.
- Language and digital literacy barriers restrict access to reliable healthcare guidance.
- Coordination between frontline health workers, doctors, hospitals, and administrators is limited.
- Emerging regional health risks are hard to identify, and preventive information is hard to communicate in time.

Together, these challenges can result in delayed healthcare access, increased financial burden, poor awareness of available benefits, and missed opportunities for preventive action.

**What is needed** is an integrated, multilingual, AI-driven healthcare ecosystem that makes healthcare more accessible, connected, and proactive.

---

## ✨ Features

### 🤖 Multilingual AI Healthcare Assistant

A conversational assistant powered by Google Gemini and built with LangChain and LangGraph. It provides general healthcare guidance, symptom-related information, and preventive recommendations, and helps users understand appropriate next steps. Conversations are contextual and supported in nine Indian languages. The assistant is connected to hospital discovery and government scheme information, so a single conversation can move naturally from a health question to finding a facility or a relevant scheme.

### 🏛️ Government Scheme Intelligence

A Retrieval-Augmented Generation (RAG) system that makes government healthcare schemes easier to discover and understand. It retrieves relevant information from scheme knowledge sources, explains eligibility criteria and available benefits, and helps users understand application procedures. This information is integrated directly into the assistant's answers.

Built with **Qdrant**, **Jina Embeddings**, and **Cohere Reranking**.

### 📞 AI-Powered Voice Calling Agent

A voice-first system designed to bridge the digital accessibility gap. Citizens can get healthcare assistance through an ordinary phone call, with multilingual voice interaction, instead of navigating a website or smartphone app. This is especially useful for elderly citizens and people with limited digital literacy.

Access to healthcare information should not depend on owning or understanding a smartphone.

Built with **Exotel** and **Sarvam AI**.

### 🦠 Proactive Disease Surveillance and Early Warning

An AI-powered public-health intelligence system that connects community health reports with regional weather and environmental information. It works in four steps:

1. Frontline health workers submit community-level health reports.
2. Doctors review and validate the submitted information.
3. The proactive intelligence engine analyzes the validated reports alongside weather and environmental conditions.
4. Gemini generates location-specific preventive health advisories and alerts.

**Example: dengue risk intelligence.** When frontline workers report increasing fever cases and doctors validate a dengue-related pattern, the system combines these reports with environmental indicators such as rainfall and humidity. It then identifies potential regional risk and generates relevant dengue-prevention advisories. This supports a shift from reactive healthcare towards proactive disease awareness and prevention.

#### 📸 Proof on Live Data

The early-warning engine has been run on live data, not only on test inputs. On **25 August 2026**, the system generated an **AI Outbreak Advisory** for Ahmedabad, Gujarat. It flagged an elevated index for **Dengue Fever (DENV-2 serotype)** and **Chikungunya**, linked it to humidity and temperature conditions that favor mosquito breeding, listed high-priority symptoms and emergency red flags, and produced a household and community action protocol that can be broadcast to citizens and ASHA workers.

On **30 August**, TV9 Gujarati reported a dengue surge in Ahmedabad, with more than 1,000 dengue cases recorded in the preceding month. This is consistent with the risk the advisory had flagged days earlier.

Image: https://drive.google.com/drive/folders/1c6qyOhUocQugr_dbDT7gHkH6QStmjscn

*Top: the AI Outbreak Advisory generated by BharatSwasthya AI for Ahmedabad. Bottom: TV9 Gujarati news coverage of rising dengue cases in the city.*

> The advisory is a preventive, decision-support output based on validated reports and environmental data. It is not a diagnosis or a confirmed outbreak declaration.

### 🏥 Hospital Bed Availability and Resource Explorer

A location-based discovery system that helps citizens find suitable medical facilities. Users can see nearby hospitals along with general and ICU bed availability, including total, occupied, and vacant capacity. Ward charges are displayed where the information is available. Hospitals manage their own information through dedicated portals, and users can navigate to a facility through Google Maps integration.

### 👨‍⚕️ Healthcare Worker and Administration Portals

Dedicated portals connect the stakeholders involved in community healthcare management, creating a connected flow of information from communities up to administrators.

| Stakeholder | Responsibilities |
|:--|:--|
| 🧑‍⚕️ **Frontline Health Workers** | Submit community-level health reports. |
| 👨‍⚕️ **Doctors** | Review and validate submitted reports. |
| 🏥 **Hospitals** | Manage hospital profiles and bed availability. |
| 🧑‍💼 **Administrators** | Monitor health reports, disease information, and proactive alerts. |

### 🚑 Emergency Assistance and Preventive Alerts

Essential healthcare information and emergency help are made easier to reach. Users get quick access to India's 108 ambulance service, along with preventive healthcare information and proactive regional health advisories.

### 🔗 Agentic AI Integration and Workflow Testing

Rather than treating AI capabilities as isolated modules, BharatSwasthya AI connects them into coordinated workflows. LangGraph handles agentic workflow orchestration and tool interactions, bringing together multiple AI services, APIs, and external capabilities. Services are developed, integrated, and tested through AgentFoundry IDE, where workflow testing verifies that platform components communicate correctly.

Built with **AgentFoundry IDE**, **LangChain**, **LangGraph**, and **Google Gemini**.

---

## 🔄 How It Works

BharatSwasthya AI connects community-level healthcare information with AI-powered intelligence and citizen-facing services. There are two main flows.

### Community Health Intelligence Flow

Health information travels from the field to citizens as preventive alerts:

1. **Frontline Health Workers** collect and submit **community health reports**.
2. **Doctors** review and validate the reports, producing **validated health reports**.
3. The **proactive AI intelligence engine** receives the validated reports together with **weather and environmental data**.
4. The engine performs a **regional health risk analysis**.
5. **Gemini** generates **location-specific advisories**.
6. **Preventive health alerts** reach citizens, supporting awareness and prevention.

### Citizen Access Flow

Citizens reach the same connected services through two channels:

- **📞 Voice calling:** the citizen calls and speaks with the **AI Voice Agent**.
- **💻 Website:** the citizen chats with the **AI Healthcare Assistant**.

Both channels connect to the same set of services:

- Healthcare guidance
- Government scheme intelligence
- Hospital discovery
- Preventive health information

### Connected Stakeholder Ecosystem

| Stakeholder | Platform interaction |
|:--|:--|
| 🙋 **Citizens** | Access healthcare assistance, schemes, hospitals, and preventive information. |
| 🧑‍⚕️ **Health Workers** | Report community health conditions. |
| 👨‍⚕️ **Doctors** | Validate health reports and medical information. |
| 🏥 **Hospitals** | Update healthcare resources and bed availability. |
| 🧑‍💼 **Administrators** | Monitor community health information and regional alerts. |
| 🤖 **AI Services** | Process information, coordinate workflows, and generate relevant intelligence. |

---

## 🛠️ Built With

The platform combines modern web technologies, AI orchestration frameworks, retrieval infrastructure, and voice communication services.

| Category | Technologies |
|:--|:--|
| 🎨 **Frontend** | React.js, Vite, Tailwind CSS |
| ⚙️ **Backend** | Node.js, Express.js |
| 🗄️ **Database** | MongoDB |
| 🐍 **AI Services** | Python, FastAPI |
| 🕸️ **Agentic AI** | AgentFoundry IDE, LangChain, LangGraph |
| 🧠 **Large Language Model** | Google Gemini |
| 🔎 **Vector Database** | Qdrant |
| 🔤 **Embeddings** | Jina Embeddings |
| 📈 **Reranking** | Cohere Reranking |
| 🎙️ **Voice AI** | Exotel, Sarvam AI |
| 🌦️ **Weather Intelligence** | Open-Meteo |
| 🗺️ **Maps and Navigation** | Google Maps APIs |

**How the pieces fit together**

- React, Vite, and Tailwind CSS build the interactive frontend and the stakeholder portals.
- Node.js and Express.js handle backend APIs and application services, with MongoDB storing application and healthcare data.
- Python and FastAPI run the separate AI-powered services.
- LangChain and LangGraph orchestrate agents and tool interactions, with Google Gemini powering conversation and AI-generated health intelligence.
- Qdrant provides vector-based retrieval, Jina Embeddings represent scheme information semantically, and Cohere Reranking improves the relevance of what is retrieved.
- Exotel and Sarvam AI enable voice-based interactions.
- Open-Meteo supplies weather data, and Google Maps APIs power hospital discovery and navigation.

---

## 🌟 Why It Stands Out

The primary innovation of BharatSwasthya AI is not any individual AI feature, but the **integration of multiple healthcare services into one connected ecosystem**.

| Conventional challenge | Our approach |
|:--|:--|
| Fragmented healthcare information | Unified healthcare information ecosystem |
| Application-dependent accessibility | Website and ordinary phone-call access |
| Difficulty understanding healthcare schemes | RAG-powered scheme intelligence |
| Disconnected community health reporting | Connected health worker and doctor portals |
| Limited regional health intelligence | AI-assisted analysis of validated reports and environmental conditions |
| Limited hospital resource visibility | Location-based hospital and bed discovery |
| Isolated AI capabilities | Coordinated agentic AI workflows |

### 📞💻 Voice plus Web Access

Our strongest differentiator is offering two complementary access channels. **Voice-first access** lets citizens get healthcare assistance through ordinary phone calls, while **digital access** lets website users explore services and interact with the AI assistant. Together they make healthcare information inclusive for people with different levels of digital literacy, language preferences, and technology access.

---

## 📊 Scale of the Problem

Healthcare accessibility, affordability, awareness, and preventive care remain significant challenges in India. A few indicators show the scale:

| Indicator | Reported figure |
|:--|:--|
| 💸 **Out-of-pocket expenditure** | 43.4% of India's total health expenditure (National Health Accounts Estimates 2022-23) |
| 🧑‍⚕️ **ASHA workforce** | Over 10 lakh frontline ASHA workers |
| 🏛️ **PM-JAY awareness** | 62% awareness among surveyed respondents in a six-state study |

These numbers point to several consequences:

- **Financial barriers:** high out-of-pocket expenditure increases the burden on households.
- **Awareness gaps:** limited understanding of government schemes can prevent citizens from accessing benefits they are entitled to.
- **Accessibility barriers:** language and digital literacy challenges restrict access to healthcare information.
- **Coordination gaps:** disconnected health reporting can delay identification of emerging health concerns.
- **Resource visibility:** limited information about hospital resources makes facility discovery harder.

The problem is therefore not simply the availability of healthcare services, but the lack of effective coordination, accessibility, and proactive intelligence across the existing healthcare ecosystem.

---

## 🎯 Expected Impact

| Beneficiary | Expected impact |
|:--|:--|
| 🙋 **Citizens** | Better access to multilingual healthcare guidance, schemes, and hospital discovery. |
| 🌾 **Rural Communities** | Healthcare assistance through voice-based interactions. |
| 🧑‍⚕️ **ASHA and Frontline Workers** | Digital community health reporting and improved coordination. |
| 👨‍⚕️ **Doctors** | Improved visibility and validation of community health information. |
| 🏥 **Hospitals** | Better visibility and management of healthcare resources. |
| 🧑‍💼 **Public-Health Administrators** | Monitoring of health reports, regional risks, and preventive advisories. |

**Expected outcomes**

- Reduced effort in finding relevant healthcare information and nearby facilities
- Improved awareness of government healthcare schemes
- Increased accessibility through multilingual voice interactions
- Better coordination between frontline health workers, doctors, and administrators
- Faster communication of preventive health advisories
- Improved visibility into hospital resource availability
- Support for proactive identification of potential regional disease risks

> These are expected outcomes, not independently measured impact figures.

---

## 🚀 Deployment and Scalability

BharatSwasthya AI has been developed as a full-stack healthcare platform with a web application, backend services, and separate AI-powered services.

| Component | Technology / Infrastructure |
|:--|:--|
| 🎨 **Frontend** | React application, Vercel |
| ⚙️ **Backend** | Node.js, Express.js |
| 🗄️ **Database** | MongoDB |
| 🐍 **AI Services** | Python, FastAPI |
| 🕸️ **Agentic Workflows** | LangGraph |
| 🔎 **Knowledge Retrieval** | Qdrant |
| 🎙️ **Voice Communication** | Exotel, Sarvam AI |
| 🌐 **External Intelligence** | Open-Meteo, Google Maps APIs |

The modular architecture allows the platform to expand across districts and states by onboarding:

- Additional hospitals and healthcare facilities
- More frontline health workers and doctors
- Additional regional health information sources
- More Indian languages
- New AI-powered healthcare and administrative services

---

## 🔮 Future Vision

Our vision is a unified, intelligent healthcare ecosystem for India where technology bridges every gap between citizens and healthcare services. We aspire to empower communities through multilingual AI, voice-first accessibility, connected healthcare networks, and proactive disease intelligence.

By connecting citizens, frontline workers, doctors, hospitals, and public-health administrators, BharatSwasthya AI aims to transform healthcare from fragmented and reactive services into a seamless, inclusive, and preventive ecosystem that reaches every corner of India.

---

## 👥 Team HemaVajra

| Team Member | GitHub Profile |
|:--|:--|
| **Harit Adesara** | [@harit-adesara](https://github.com/harit-adesara) |
| **Fenil Koshti** | [@Fenil-1807](https://github.com/Fenil-1807) |

---

## 🔗 Project Links

| Resource | Link |
|:--|:--|
| 💻 **GitHub Repository** | [https://github.com/Fenil-1807/Bharat_Swasthaya_Full.git](#) |
| 🎬 **Project Demo and Videos** | [https://decode-sih-website.vercel.app](#) |

---

## 📚 References

1. Ministry of Health and Family Welfare, Government of India. *Annual Report 2023-24*, Chapter 6: E-Governance and Telemedicine.
2. *National Health Accounts Estimates 2022-23*. Healthcare expenditure and out-of-pocket expenditure statistics.
3. *Awareness of India's National Health Insurance Scheme (PM-JAY): A Cross-sectional Study Across Six States* (2023).
4. National Health Mission (NHM). Official NHM-MIS data.
5. International Journal of Creative Research Thoughts (2026). *Disparities in Healthcare Accessibility Between Rural and Urban Communities*.
6. Ballard Brief. *Healthcare Access in Rural Communities in India*.
7. Algondi, N. A. (2025). "Multilingual Voice AI Assistants for Bridging Language Gaps in Rural Healthcare." *International Journal of Scientific Research and Engineering Trends*, 11(2).
8. Shenoy and D'Souza (2026). "Role of ASHA Workers in Empowering Community Health through ICT." *International Journal of Social Science Research*.

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

**BharatSwasthya AI: Connecting Healthcare. Empowering Communities. Building a Healthier India.**

Built with ❤️ by Team HemaVajra.
