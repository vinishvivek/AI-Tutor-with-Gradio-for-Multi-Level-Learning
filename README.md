# 🧠 AI Tutor — Multi-Level Learning with LLMs

## 🚀 Overview

AI Tutor is an **interactive AI-powered learning application** that adapts explanations dynamically based on the learner’s level — from a **5-year-old beginner to an Einstein-level PhD thinker**.

The system is built using a **modular LLM pipeline**, combining:

* Level-aware prompt engineering
* Streaming response generation
* Structured markdown outputs
* A real-time Gradio interface

This project demonstrates how to transform a simple LLM prototype into a **production-style, modular AI system**.

---

## 🎯 Problem Statement

Learning complex topics is often:

* Too generic (same explanation for everyone)
* Not adapted to the learner’s level
* Either too simplified or overly complex

This project explores how AI can:

1. Dynamically adjust explanation depth
2. Provide structured and intuitive learning outputs
3. Deliver real-time, interactive tutoring experiences

---

## 🎚️ Demo

### Input Interface

* Enter topic + question
* Select explanation level via slider

### Streaming Response

* AI generates responses **token-by-token** with a streaming response
* Output structured in markdown:

```
## Explanation
## Example
## Follow-up Question
```

---

## 🧠 Solution Architecture

The system is designed as a **layered AI pipeline**, ensuring separation of concerns and extensibility.

### 🔄 Flow

```
User Input (UI)
   ↓
Validation Layer
   ↓
Tutor Service (Orchestration)
   ↓
Prompt Builder (Level-aware logic)
   ↓
OpenAI Gateway (Streaming LLM call)
   ↓
Token Stream → UI (Live Rendering)
```

---

## 🏗️ Project Structure

```
ai_tutor/
├── app/
│   ├── main.py                 # App assembly
│   ├── config/
│   │   └── settings.py         # Environment config
│   ├── clients/
│   │   └── openai_client.py    # LLM gateway (stream + non-stream)
│   ├── domain/
│   │   └── models.py           # Request/response schemas
│   ├── prompts/
│   │   └── tutor_prompts.py    # Prompt engineering logic
│   ├── services/
│   │   └── tutor_service.py    # Core orchestration layer
│   ├── ui/
│   │   └── gradio_app.py       # UI + streaming handler
│   └── utils/
│       └── logger.py           # Logging utility
│
├── run.py                      # Entry point
├── .env.example               # Environment variables template
└── README.md
```

---

## ⚙️ Tech Stack

* **Python**
* **OpenAI (GPT-5.4-mini / GPT-4o family)**
* **Gradio** (UI Layer)
* **Pydantic** (Data validation)
* **dotenv / pydantic-settings** (Configuration)
* **httpx** (Underlying client)

---

## 🧪 Features

* 🎚️ **Dynamic Learning Levels (1–5 Slider)**

  * 1 → 5-year-old explanation
  * 5 → Einstein-level deep reasoning

* ⚡ **Streaming Responses**

  * Token-by-token generation for real-time UX

* 🧠 **Prompt Engineering Layer**

  * Level-specific instruction injection

* 📝 **Structured Output**

  * Markdown-formatted responses

* 🧩 **Modular Architecture**

  * UI, service, prompts, and client fully decoupled

* 🔒 **Input Validation**

  * Clean user feedback for invalid inputs

* 📊 **Extensible Design**

  * Easy to plug in RAG, memory, or alternate LLM providers

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/vinishvivek/AI-Tutor-with-Gradio-for-Multi-Level-Learning.git
cd AI-Tutor-with-Gradio-for-Multi-Level-Learning
```

---

### 2. Create environment

```bash
conda create -n ai_tutor python=3.11
conda activate ai_tutor
```

or

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure environment variables

Create a `.env` file:

```text
OPENAI_API_KEY=your_api_key_here
LLM_MODEL=gpt-5.4-mini
```

---

### 5. Run the app

```bash
python run.py
```

Then open:

```
http://127.0.0.1:7860
```

---

## ⚠️ Limitations

* Output quality depends on prompt effectiveness
* Streaming may vary slightly depending on model/provider
* No conversation memory (single-turn interaction)
* Responses are educational, not authoritative

---

## 🔧 Engineering Highlights

This project focuses on **AI system design**, not just model usage:

* ✅ Streaming-first architecture
* ✅ Clear separation of concerns
* ✅ Prompt engineering abstraction
* ✅ Typed request/response modeling
* ✅ Service-layer orchestration
* ✅ UI decoupled from business logic
* ✅ Clean error handling and logging

---

## 🚀 Future Improvements

* Multi-turn conversation memory
* Quiz / assessment mode
* RAG-based learning from documents
* User personalization
* Cost/token monitoring
* Deployment (Docker / Hugging Face Spaces)
* API layer (FastAPI backend)

---

## 📌 Key Takeaway

This project is not just about tutoring.

It demonstrates how to:

> Build a **modular, production-ready AI application** that delivers
> real-time responses, structured outputs, and scalable architecture.

---

## 👤 Author

**Vinish Vivek**

AI Engineer | LLM Systems | RAG Pipelines | Applied AI Development

---

## ⭐ If you found this useful

Consider starring the repo — or better, fork it and build your own version 🚀

---
