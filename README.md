# 🧠 AI Agents

A collection of AI agents built using Large Language Models (LLMs) to solve real-world problems through reasoning, tool usage, and multimodal inputs.

---

## 🚀 Overview

This repository contains modular AI agents, each designed for a specific task such as image understanding, web search, and automation.

New agents will be continuously added to expand capabilities.

---

## 🤖 Available Agents

### 👨‍🍳 Personal Chef Agent

* Takes a **fridge image as input**
* Detects visible ingredients using vision models
* Uses web search to suggest recipes
* Returns 2–3 practical meal ideas

---

## ⚙️ Setup

### 1. Install dependencies

```
pip install -r requirements.txt
```

---

### 2. Create your own environment variables

⚠️ **Important:**

* API keys are **required** to run the project

Create a `.env` file in the root directory and add:

```
OPENAI_API_KEY=your_openai_api_key
TAVILY_API_KEY=your_tavily_api_key
```

---

## 🔑 API Keys Required

This project uses external services, so you need to generate your own API keys:

* OpenAI API key → for LLM and vision capabilities
* Tavily API key → for web search

---

## 🧠 Key Concepts

* Multimodal AI (image-based input)
* Agent-based architecture
* Tool calling (web search integration)
* Prompt engineering
* Real-time data retrieval

---

## ⚠️ Limitations

* Image recognition depends on clarity and visibility
* Some ingredients may be marked as "uncertain"
* External API limits may affect performance

---

## 🔮 Roadmap

Planned additions:

* 📊 Data Analysis Agent
* 📄 Document Q&A Agent
* 🤖 Multi-agent workflows

---
