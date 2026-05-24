<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=2,12,24&height=200&section=header&text=🤖%20Agno%20Multi-Agent%20System&fontSize=44&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Finance%20|%20Memory%20|%20File%20Gen%20|%20Multi-Language%20Team%20—%20Powered%20by%20Groq%20+%20Qwen3&descAlignY=60&descAlign=50" width="100%"/>

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Agno](https://img.shields.io/badge/Agno-Framework-6C63FF?style=for-the-badge&logo=abstract&logoColor=white)](https://github.com/agno-agi/agno)
[![Groq](https://img.shields.io/badge/Groq-Qwen3--32b-F55036?style=for-the-badge&logo=lightning&logoColor=white)](https://groq.com)
[![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://sqlite.org)
[![YFinance](https://img.shields.io/badge/YFinance-Stock%20Data-00C805?style=for-the-badge&logo=yahoo&logoColor=white)](https://pypi.org/project/yfinance/)
[![ReportLab](https://img.shields.io/badge/ReportLab-PDF%20Gen-E63946?style=for-the-badge&logo=adobeacrobatreader&logoColor=white)](https://www.reportlab.com)
[![License](https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge)](LICENSE)

---

## 📌 Project Overview

A production-ready **multi-agent AI system** built on the **Agno framework** with **Groq's Qwen3-32b** as the backbone LLM. This project demonstrates four specialized agent architectures working independently and collaboratively — from real-time stock analysis to persistent memory, PDF generation, and multilingual team coordination.

> **"Not just one agent — a full ecosystem."**

---

## 🔄 Pipeline Workflow

```
User Query → Agent Router → Specialized Agent → Tool Execution → Response / File / Memory
```

### 1️⃣ Finance Agent
- Fetches live stock data via **YFinanceTools**
- Researches analyst recommendations via **DuckDuckGoTools**
- Returns structured markdown tables with real-time insights

### 2️⃣ Memory Agent
- Maintains **user-specific long-term memory** via SQLite (`agno.db.sqlite`)
- Persists facts across sessions with `enable_user_memories=True`
- User context retrieved by `user_id` across conversations

### 3️⃣ File Generation Agent
- Generates structured PDFs (reports, summaries) via **ReportLab + FileGenerationTools**
- Saves output files to local directory with metadata (filename, size, URL)

### 4️⃣ Multi-Language Team
- **Team of 3 agents**: English, Hindi, Gujarati specialists
- Coordinated by a **Team Leader** with `show_members_responses=True`
- All members answer in parallel — no single-agent routing

---

## 🤖 Agent Breakdown

### 1️⃣ Finance Agent
```python
tools=[YFinanceTools(), DuckDuckGoTools()]
model=Groq(id="qwen/qwen3-32b")
```
- Real-time stock price + analyst consensus
- Outputs markdown tables for clean readability
- Combines structured financial data with web research

### 2️⃣ Memory Agent
```python
db=SqliteDb(db_file="tmp/memory.db")
enable_user_memories=True
add_history_to_context=True
```
- Stores user profile facts across sessions
- Retrieves memories using `get_user_memories(user_id=...)`
- Clears and rebuilds cleanly via `db.clear_memories()`

### 3️⃣ File Generation Agent ⭐ Most Versatile
```python
tools=[FileGenerationTools(output_directory="tmp")]
db=SqliteDb(db_file="tmp/test.db")
```
- Creates PDFs, reports, and structured documents on demand
- Returns file metadata: `filename`, `size`, `url`
- Backed by persistent session DB for context continuity

### 4️⃣ Multi-Language Team
```python
team=Team(members=[english_agent, hindi_agent, gujarati_agent])
model=Groq(id="qwen/qwen3-32b")
show_members_responses=True
```
- Team Leader coordinates all agents simultaneously
- Each agent answers in its designated language
- Enforced via system instructions — no single-agent fallback

---

## 📊 Agent Capability Matrix

| Agent | Tool Use | Memory | File Output | Multi-Agent |
|:---|:---:|:---:|:---:|:---:|
| Finance Agent | ✅ YFinance + DDG | ❌ | ❌ | ❌ |
| Memory Agent | ❌ | ✅ SQLite | ❌ | ❌ |
| File Gen Agent | ✅ FileGen | ✅ SQLite | ✅ PDF | ❌ |
| 🏆 **Language Team** | ❌ | ❌ | ❌ | ✅ 3-Agent |

---

## 🔍 Key Insights

- 🧠 **Persistent memory** is scoped per `user_id` — multiple users can co-exist in the same SQLite DB without interference
- 📈 **Qwen3-32b via Groq** delivers near-instant inference, making real-time stock agents practical without API cost overhead
- 🌐 **Team coordination** with `show_members_responses=True` ensures all agent outputs are surfaced — critical for multilingual use cases
- 🗂️ **FileGenerationTools** returns a `files` object with metadata — enabling downstream automation (upload, email, store)
- ⚡ `add_datetime_to_context=True` gives agents temporal awareness without hardcoding date logic

---

## 🗂️ Repository Structure

```
agno-multi-agent-system/
├── Agent.py              # File Generation Agent (PDF reports)
├── Finance.py            # Finance Agent (stocks + web research)
├── Memory.py             # Memory Agent (persistent user context)
├── Team.py               # Multi-Language Team (EN / HI / GU)
├── requirements.txt      # Python dependencies
├── memory.db             # SQLite memory store (auto-generated)
├── tmp/                  # Generated files output directory
└── README.md
```

---

## 🚀 Quick Start

```bash
# Clone the repo
git clone https://github.com/ronakrajput8882/Agno-Multi-Agent-System.git
cd Agno-Multi-Agent-System

# Install dependencies
pip install -r requirements.txt

# Set up environment
echo "GROQ_API_KEY=your_key_here" > .env

# Run any agent
python Finance.py       # Live stock analysis
python Memory.py        # Persistent memory demo
python Agent.py         # PDF report generation
python Team.py          # Multilingual team response
```

---

## 🧠 Key Learnings

- Agno's `Team` abstraction enables true parallel multi-agent execution with a single `print_response()` call
- SQLite as an agent memory backend is zero-infra — no Redis, no vector DB needed for user-scoped fact storage
- `FileGenerationTools` abstracts away all PDF boilerplate — just describe what you want, get a file back
- Groq's ultra-low latency makes Qwen3-32b viable for interactive, real-time agent workflows
- Scoping memory by `user_id` is the foundation for multi-tenant agent applications

---

## 🛠️ Tech Stack

| Tool | Use |
|:---|:---|
| Agno | Multi-agent orchestration framework |
| Groq + Qwen3-32b | Inference backbone (ultra-low latency) |
| YFinance | Live stock data retrieval |
| DuckDuckGo Tools | Web search for analyst research |
| SQLite (agno.db) | Persistent agent memory storage |
| ReportLab | PDF file generation |
| python-dotenv | Secure API key management |
| Streamlit | (Optional) UI layer |

---

<div align="center">

### Connect with me

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/ronaksinh-rajput8882)
[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://instagram.com/techwithronak)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/ronakrajput8882)

*If you found this useful, please ⭐ the repo!*

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=2,12,24&height=100&section=footer" width="100%"/>

</div>
