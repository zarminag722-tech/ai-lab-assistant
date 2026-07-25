# 🧪 AI Lab Assistant

> An AI-powered web application designed to help university students with science and computer science lab experiments, safety procedures, and structured lab report generation.

---

## 🔗 Live Application & Links

* **Live App URL:** `https://ai-lab-assistant-gfbnnvzkauwxdqv89rh6ct.streamlit.app`
* **GitHub Repository:** `https://github.com/zarminag722-tech/ai-lab-assistant`

---

## 📌 Problem Statement & Target Audience

* **Problem:** University science and computer science students often struggle to find clear, step-by-step procedures, safety equipment guidelines, and proper academic formatting for their lab reports. Standard search results are often messy, incomplete, or lack safety protocols.
* **Solution:** **AI Lab Assistant** acts as a 24/7 personal tutor that quickly generates organized experiment guides (with safety warnings) and formats raw experimental observations into clean, academic lab reports in seconds.
* **Target Audience:** University students, lab instructors, and researchers in Chemistry, Physics, Biology, and Computer Science.

---

## ✨ Features

* **📋 Experiment Guide Generator:**
  * Instant step-by-step procedure for any university experiment.
  * Comprehensive **Safety First** warnings and required equipment list.
  * Expected observations and practical troubleshooting tips for common student mistakes.
* **📑 Lab Report Formatter:**
  * Converts rough notes, titles, aims, and raw observations into a structured academic report format.
* **⚡ High Availability & Resilience:**
  * Implemented dynamic fallback mechanisms to ensure 100% uptime without hitting model downtime errors.

---

## 🤖 The AI Feature & System Prompt

The core AI engine uses OpenRouter API to access high-performance, open-source AI models dynamically. 

### System Prompt / Core Instructions:
```text
You are an expert AI Lab Assistant for university students.
Always follow this structured response format:
1. **Safety First & Equipment**: List precautions and apparatus needed.
2. **Step-by-Step Procedure**: Clear numbered instructions.
3. **Expected Observations & Troubleshooting**: What should happen and common mistakes.

Keep explanations clear, structured, and academic.
