# 🔎 Search & Weather AI Agent

An **Agentic AI application** that intelligently decides when to use web search or weather tools to answer user queries. Built with **LangChain, Groq, Tavily, Weatherstack, and Streamlit**.

---
## 🚀 Project Overview

This project demonstrates how an LLM-powered agent can **reason about a user's request, select the appropriate tool, execute it, and generate a final response**.

The agent supports:

- 🔎 **Web Search** — Retrieves current information using Tavily.
- 🌤️ **Weather Information** — Fetches current weather using Weatherstack.
- 🤖 **Tool Calling** — Dynamically selects tools based on the user's query.
- 💬 **Interactive UI** — Built with Streamlit.

---
## 🏗️ Architecture

<div align="center">

<img src="assets/Search_Weather Agent Architecture.png" alt="banner">

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

| Component | Technology |
|---|---|
| Agent Orchestration | LangChain — `create_agent()` |
| LLM | Groq — `openai/gpt-oss-20b` |
| Web Search Tool | Tavily Search |
| Weather Tool | Weatherstack API + custom LangChain tool |
| Tool Calling | LangChain Tool Calling |
| Agent Logic | Python |
| Frontend | Streamlit |
| API Integration | Requests |
| Configuration | python-dotenv + `.env` |
| SSL / Certificates | Certifi |

---
## 📊 Example Interaction

**User Question:** 
```bash
    What is the capital of Bangladesh and what is weather of right now?
```
**Search & Weather AI Agent:**
```bash
The capital of Bangladesh is Dhaka.  
    Current weather in Dhaka:  
    - Temperature: 30 °C  
    - Condition: Smoky haze  
    - Humidity: 60 %
```


## ⚙️ Setup

### Prerequisites

- Python 3.11
- `conda` or any Python virtual environment manager

### 🚀 𝙃𝙤𝙬 𝙩𝙤 𝙍𝙪𝙣 𝙩𝙝𝙚 𝘼𝙥𝙥𝙡𝙞𝙘𝙖𝙩𝙞𝙤𝙣

### 1️⃣ Clone the Repository

```
    git clone https://github.com/KzRaihan/Search-Weather-AI-Agent.git

```

### 2️⃣ Create and activate an environment

```
    conda create -n AI_Agent python=3.11 -y
    conda activate AI_Agent

```

### 3️⃣ Install Dependencies

```
    pip install -r requirements.txt
```

### 4️⃣ Configuration

Create a `.env` file at the repository root and add your API keys:

```bash
    OPENAI_API_KEY="your-openai-api-key"
    TAVILY_API_KEY="your-tavily-api-key"
    WEATHERSTACK_API_KEY="your-weatherstack-api-key"
```

> Do not commit your `.env` file or secret keys to source control.

### Run the Project

Use one of the Python entrypoints:

```bash
    streamlit run app.py
```

### Notebook Exploration

Open the research notebook for additional agent demos and experiments:

```bash
jupyter notebook research/agent_experiment.ipynb
```
---
## Project Structure

```text
.
├── .env
├── README.md
├── app.py
├── main.py
├── requirements.txt
└── research/
    └── agent_experiment.ipynb
```
---
## Contribution 

Contributions are welcome. If you'd like to improve this repo, open an issue or submit a pull request with enhancements, bug fixes, or documentation improvements.


---
## 👨‍💻 Author

**Md Kamruzzaman** __ AI/ML Engineer
[GitHub](https://github.com/KzRaihan) · [LinkedIn](https://www.linkedin.com/in/kzraihan/)

---
