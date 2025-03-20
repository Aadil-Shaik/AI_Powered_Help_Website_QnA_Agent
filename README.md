# AI-Powered Help Website Q&A Agent

## Overview
This project is an **AI-powered question-answering agent** that processes documentation from help websites and accurately answers user queries about **product features, integrations, and functionality**. The agent performs **recursive web crawling**, extracts structured documentation, indexes it using **semantic search**, and generates precise responses using **Gemini AI**.

## Features
- ✅ Accepts a **help website URL** and crawls documentation pages recursively.
- ✅ Extracts **meaningful content** while filtering out navigation elements.
- ✅ Implements **semantic search** to find the most relevant documentation.
- ✅ Calls **Gemini AI** to generate **clear and precise answers**.
- ✅ Provides **source references** where applicable.
- ✅ Handles **network errors and unsupported websites** gracefully.
- ✅ Uses **unit tests** to validate functionality.

---

## 📂 Installation and Setup
### **🔹 Clone the Repository**
```powershell
git clone <your-private-repo-url>
cd ai-helpdesk-bot
```
## (I am using windows powershell in this case)

### **🔹 Set Up a Virtual Environment**
```powershell
python -m venv venv
```
### **🔹 Activate the Virtual Environment**
**PowerShell (Windows):**
```powershell
.venv\Scripts\Activate.ps1
```
**Mac/Linux:**
```bash
source venv/bin/activate
```

### **🔹 Install Dependencies**
```powershell
pip install requests beautifulsoup4 sentence-transformers numpy google-generativeai
```

### **🔹 Set Up Gemini API Key**
```powershell
$env:GEMINI_API_KEY = "your_api_key_here"
```

---

## 🚀 Running the Application

### **🔹 Execution Steps**
After installing dependencies, **run the agent** with a help website URL:
```powershell
python src/qa_agent.py --url https://help.slack.com
```

### **🔹 Example Terminal Execution**
```powershell
(.venv) PS C:\Users\AADIL SHAIK\OneDrive\Desktop\Pulse project> python src/qa_agent.py --url https://help.slack.com
> 
Crawling website...
Processing content...
Building index...
Extracted Documents:
URL: https://help.slack.com
Snippet: Hi, how can we help? Common troubleshooting topics: notifications, connecting to Slack, huddles
-----
Agent is ready! Type a question (type 'exit' to quit):

> How do I create a channel on Slack?
I am sorry, but I cannot answer your question. However, related topics include "channel management", "moving channels", "shared channels", "public channels", and "private channels."

> How do I troubleshoot Slack connectivity issues?
To troubleshoot Slack connectivity issues, here are some common topics and potential solutions:
- **Check your internet connection:** Ensure you have a stable and active internet connection.
- **Whitelisting:** Ensure that Slack is whitelisted in your firewall or antivirus software.
- **Connecting:** Refer to the "connecting to Slack" topic for general guidance.

> How can I integrate Slack with other apps?      
To integrate Slack with other apps, you can connect, simplify, and automate using apps and tools. The context mentions several apps that can be integrated with Slack, such as Asana, Bitbucket, Dropbox, GitHub, Google Calendar, Jira, OneDrive, Zapier, Zoom, etc.
```

---

## 🔬 Running Unit Tests
Unit tests validate **crawling, processing, and semantic search**.

### **🔹 Run All Tests**
```powershell
python -m unittest discover tests
```

### **🔹 Run a Specific Test**
For example, test **query processing**:
```powershell
python -m unittest tests/test_query.py
```

### **📌 Sample Unit Test Output**
```powershell
Ran 3 tests in 1.2s
OK
```

---

## ✅ Features Implemented vs. Assignment Requirements
| **Requirement** | **Implemented?** | **Notes** |
|---------------|---------------|------------|
| **Crawl a help website URL** | ✅ Yes | Recursive crawling with filtering |
| **Process and index documentation** | ✅ Yes | Extracts structured content, filters navigation |
| **Accept user queries** | ✅ Yes | Terminal-based Q&A session |
| **Provide accurate answers** | ✅ Partially | Some responses need better retrieval |
| **Handle missing information** | ✅ Yes | Returns relevant topics when an answer is missing |
| **Indicate source references** | ✅ Yes | Includes URLs where possible |
| **Graceful error handling** | ✅ Yes | Handles invalid URLs, network issues |
| **Performance benchmarks** | ✅ Yes | Added logging for execution time |
| **Unit tests** | ✅ Yes | Covers crawling, processing, and search |
| **Dockerization** (Bonus) | ❌ No | Could be added later |
| **API Endpoint** (Bonus) | ❌ No | CLI-based for now |
| **Multi-source support** (Bonus) | ❌ No | Currently supports a single website at a time |

---

## 📑 Documentation
### **1️⃣ Technical Architecture Overview**
- **Crawler** (`crawler.py`): Recursively extracts documentation pages.
- **Processor** (`processor.py`): Cleans HTML, extracts structured content, and generates embeddings.
- **Semantic Search** (`query.py`): Uses **Sentence Transformers** for similarity matching.
- **Answer Generation** (`gemini_api.py`): Calls **Gemini AI** to refine responses.

### **2️⃣ Implementation Approach**
- **Extracts content only from structured sections** (`article`, `section`, `.help-content`).
- **Semantic search prioritizes the best-matching sections**.
- **LLM answer refinement improves response quality**.

### **3️⃣ Future Improvement Suggestions**
- **Expand to multiple documentation sources** (e.g., Slack + Google Help).
- **Enhance query understanding** (allow paraphrased questions).
- **Add API support** (for integration into web apps).

### **4️⃣ Testing Approach**
- **Unit tests** validate individual components.
- **Performance benchmarks** track speed of crawling, processing, and answering.

---

## 📚 Third-Party Libraries Used
| Library | Purpose |
|---------|---------|
| `requests` | Fetches web pages |
| `beautifulsoup4` | Parses and cleans HTML |
| `sentence-transformers` | Generates embeddings for search |
| `numpy` | Computes similarity scores |
| `google-generativeai` | Calls Gemini AI for answer refinement |

---

## ⚠️ Assumptions & Limitations
### **🔹 Assumptions**
- Help websites contain structured **documentation sections** (`article`, `section`).
- Queries are **clear and concise**.

### **🔹 Limitations**
- **Dynamic content is not fully handled** (JavaScript-rendered content is not fetched).
- **Crawling is limited to avoid excessive server requests**.

---

#### Contributors: Aadil Shaik
