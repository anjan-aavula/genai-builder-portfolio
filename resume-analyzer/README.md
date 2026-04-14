# Resume RAG App (GenAI Project)

## 📌 Overview

This project is a simple **Retrieval-Augmented Generation (RAG)** application that allows you to:

* Load your resume
* Ask questions about it
* Get intelligent answers using OpenAI models

---

## 🧠 How It Works

1. **Load Resume**

   * Extracts text from your PDF

2. **Chunking**

   * Splits text into smaller parts

3. **Embeddings**

   * Converts chunks into vector representations

4. **Vector Search (FAISS)**

   * Finds the most relevant parts of your resume

5. **LLM Response**

   * Sends context + question to OpenAI to generate answers

---

## 🚀 Setup Instructions

### 1. Clone or create project

```bash
mkdir resume-rag-app
cd resume-rag-app
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Add your API key

Create a `.env` file:

```
OPENAI_API_KEY=your_key_here
```

---

### 4. Add your resume

Place your file as:

```
resume.pdf
```

---

### 5. Run the app

```bash
python app.py
```

---

## 💬 Example Questions

* What are my key skills?
* Summarize my experience
* What roles am I suited for?
* Do I have experience in Python?

---

## ⚠️ Notes

* Works best with text-based PDFs
* Avoid scanned resumes (OCR not included)
* Embeddings cost is low but not free

---

## 🔮 Future Improvements

* Add Streamlit UI
* Support multiple documents
* Use a cloud vector database (Pinecone, Weaviate)
* Add chat history (memory)
* Job description matching

---

## 🧑‍💻 Tech Stack

* Python
* OpenAI API
* FAISS (vector search)
* NumPy
* PyPDF

---

## 🎯 Goal

This project is a beginner-friendly introduction to:

* Generative AI
* Embeddings
* Semantic search
* RAG systems

---

Happy building 🚀
