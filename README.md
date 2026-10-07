# 🔎 Search & Weather AI Agent

An **Agentic AI application** that intelligently decides when to use web search or weather tools to answer user queries. Built with **LangChain, Groq, Tavily, Weatherstack, and Streamlit**.

## 🌐 Live Demo

🚀 **[Try the Search & Weather AI Agent](https://search-weather-ai-agent-i74b.onrender.com)**

---

## 🚀 Project Overview

This project demonstrates how an LLM-powered agent can **reason about a user's request, select the appropriate tool, execute it, and generate a final response**.

The agent supports:

* 🔎 **Web Search** — Retrieves current information using Tavily.
* 🌤️ **Weather Information** — Fetches current weather using Weatherstack.
* 🤖 **Tool Calling** — Dynamically selects tools based on the user's query.
* 💬 **Interactive UI** — Built with Streamlit.

---

## 🏗️ Architecture

<div align="center">

<img src="assets/Search_Weather Agent__architecture.png" alt="Search & Weather AI Agent Architecture">

</div>

```text
User Query
     ↓
Groq LLM
     ↓
LangChain Agent
     ↓
Tool Selection
   ↙       ↘
Tavily    Weatherstack
Search       API
   ↘       ↙
    Tool Results
        ↓
   Final Response
        ↓
    Streamlit UI
```

---

## 🧩 Tech Stack

| Component           | Technology                               |
| ------------------- | ---------------------------------------- |
| Agent Orchestration | LangChain — `create_agent()`             |
| LLM                 | Groq — `openai/gpt-oss-20b`              |
| Web Search Tool     | Tavily Search                            |
| Weather Tool        | Weatherstack API + custom LangChain tool |
| Tool Calling        | LangChain Tool Calling                   |
| Agent Logic         | Python                                   |
| Frontend            | Streamlit                                |
| API Integration     | Requests                                 |
| Configuration       | python-dotenv + `.env`                   |
| SSL / Certificates  | Certifi                                  |

---

## 📊 Example Interaction

**User Question:**

```text
What is the capital of Bangladesh and what is the weather right now?
```

**Search & Weather AI Agent:**

```text
The capital of Bangladesh is Dhaka.

Current weather in Dhaka:
- Temperature: 30°C
- Condition: Smoky haze
- Humidity: 60%
```

The agent can use **multiple tools** when a query requires information from different external sources.

---

## ⚙️ Setup

### Prerequisites

* Python 3.11
* Conda or any Python virtual environment manager

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/KzRaihan/Search-Weather-AI-Agent.git
cd Search-Weather-AI-Agent
```

### 2️⃣ Create and Activate an Environment

```bash
conda create -n AI_Agent python=3.11 -y
conda activate AI_Agent
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure API Keys

Create a `.env` file at the repository root:

```env
GROQ_API_KEY="your-groq-api-key"
TAVILY_API_KEY="your-tavily-api-key"
WEATHERSTACK_API_KEY="your-weatherstack-api-key"
```

> ⚠️ **Never commit your `.env` file or API keys to source control.**

### 5️⃣ Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## ☁️ Deployment

The application is deployed on **Render** as a Web Service.

### Build Command

```bash
pip install -r requirements.txt
```

### Start Command

```bash
streamlit run app.py --server.port $PORT --server.address 0.0.0.0
```

### 🔗 Live Application

**https://search-weather-ai-agent-i74b.onrender.com**

---

## 📁 Project Structure

```text
Search-Weather-AI-Agent/
│
├── assets/
│   └── Search_Weather Agent__architecture.png
│
├── research/
│   └── agent_experiment.ipynb
│
├── .gitignore
├── README.md
├── app.py
├── main.py
└── requirements.txt
```

> `.env` is intentionally excluded from the repository for security.

---

## 🎯 Key Learning Outcomes

* Building **Agentic AI applications**
* Implementing **LLM tool calling**
* Integrating external APIs with AI agents
* Using LangChain's modern `create_agent()` architecture
* Designing dynamic tool selection
* Building interactive AI applications with Streamlit
* Deploying AI applications on Render

---

## 🤝 Contribution

Contributions are welcome. If you'd like to improve this project, feel free to open an issue or submit a pull request with enhancements, bug fixes, or documentation improvements.

---

## 👨‍💻 Author

**Md Kamruzzaman**
AI/ML Engineer

[GitHub](https://github.com/KzRaihan) · [LinkedIn](https://www.linkedin.com/in/kzraihan/)

---

⭐ If you find this project useful, consider giving it a star!
