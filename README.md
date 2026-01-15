# AI PDF Study Assistant (v2.1)

**Author:** Swapnil Tiwari  
**Degree:** B.Sc. IT (Hons.), Parul University  
**Year:** 2025–2029  

---

## 📌 About the Project

AI PDF Study Assistant is a Streamlit-based application designed to help students
analyze academic PDF documents using AI.

The application extracts text from PDFs and uses a Large Language Model (LLM)
to generate:
- Clear summaries
- Exam-oriented MCQs
- Short-answer / viva-style questions

The project is built with a strong focus on **stability, full-document processing,
and real-world deployment**.

---

## 🚀 Current Version: v2.1 (Stable)

### ✅ What v2.1 Supports
- Full PDF ingestion (any number of pages)
- Intelligent text chunking for large documents
- AI-powered **summarization**
- AI-generated **MCQs**
- AI-generated **exam-style Q&A**
- Deployed on **Streamlit Cloud**
- Secure API handling using environment secrets

> v2.1 uses **Groq LLM** for fast and reliable inference.

---

## 🧠 Version History

### v1.0
- PDF upload via Streamlit UI
- Reliable text extraction using PyPDF2
- Display of extracted PDF content
- Foundation version (no AI)

### v2.0
- Added AI-powered **PDF summarization**
- Full-document summarization using chunking
- Extended support from notes → PDFs

### v2.1 (Current)
- Added **MCQ generation**
- Added **exam / viva-style Q&A**
- Improved chunk handling and stability
- Production-ready deployment with Groq LLM

---

## 🛠️ Tech Stack

- Python
- Streamlit
- PyPDF2
- Groq LLM
- Git & GitHub

---

## 📸 Screenshots

### User Interface
![UI](screenshots/ui.png)

### Generated Output
![Output](screenshots/output.png)

---

## ▶️ How to Run Locally

```bash
git clone https://github.com/sarcasticc-git/ai-pdf-study-assistant.git
cd ai-pdf-study-assistant

python -m venv venv
venv\Scripts\activate

python -m pip install -r requirements.txt
streamlit run app.py
