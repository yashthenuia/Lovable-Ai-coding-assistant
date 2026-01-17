# 🤖 Coder Buddy (AI Coding Assistant)

Coder Buddy is an AI-powered coding assistant that works like a virtual development team.  
It converts natural language instructions into complete project structures and code files using a multi-agent workflow built with **LangGraph** and **Groq API**.

---

## 🚀 Project Overview

Coder Buddy helps developers quickly scaffold small projects such as:
- Todo applications
- Simple web apps
- Backend APIs
- Basic full-stack project structures

Instead of writing boilerplate manually, users can describe what they want in plain English, and Coder Buddy generates the project structure and source code automatically.

---

## 🧠 System Architecture

The application follows a **multi-agent architecture**:

- **Planner Agent**
  - Understands user intent
  - Breaks the request into logical steps

- **Architect Agent**
  - Designs project structure
  - Decides file layout and responsibilities

- **Coder Agent**
  - Generates actual source code
  - Writes files one by one using context from previous steps

The agents are orchestrated using **LangGraph**, ensuring controlled and sequential execution.

---

## ✨ Features

- Natural language → complete project generation
- Multi-agent reasoning for structured code output
- Supports Python backend and HTML/CSS frontend generation
- Modular, extensible architecture
- Ideal for rapid prototyping and learning

---

## 🛠️ Tech Stack

- **Python**
- **LangGraph**
- **Groq API (LLM inference)**
- **HTML / CSS (for frontend scaffolding)**
- **UV / Virtual Environment**

---

## 📂 Project Structure

```text
coder-buddy/
│
├── agents/
│   ├── planner.py
│   ├── architect.py
│   └── coder.py
│
├── prompts/
│   ├── planner_prompt.txt
│   ├── architect_prompt.txt
│   └── coder_prompt.txt
│
├── main.py
├── requirements.txt
├── .env.example
└── README.md
