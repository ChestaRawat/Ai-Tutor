# Ai-Tutor
# AI Tutor – Textbook Question Answering System (RAG)

AI Tutor is a Retrieval-Augmented Generation (RAG) based system that allows students to ask questions directly from a textbook PDF and receive accurate answers strictly based on the textbook content.  
This project is built using Class 8 Science (Chapter 1) as a sample and can be extended to any subject or textbook.

---

## Features

- Extracts text from textbook PDFs
- Splits content into paragraph-level chunks
- Generates semantic embeddings using Sentence Transformers
- Stores and retrieves embeddings using FAISS
- Answers questions using an LLM via OpenRouter API
- Ensures responses are grounded only in textbook content
- Uses simple, student-friendly language

---

## Tech Stack

- **Language:** Python  
- **PDF Processing:** PyMuPDF (fitz)  
- **Embeddings:** Sentence Transformers (`all-MiniLM-L6-v2`)  
- **Vector Database:** FAISS  
- **LLM API:** OpenRouter (Claude 3 Haiku)  
- **Data Format:** JSON  

---

## Project Workflow

1. Load the textbook PDF
2. Extract text from each page
3. Split extracted text into meaningful chunks
4. Generate embeddings for each chunk
5. Store embeddings in a FAISS index
6. Accept user questions
7. Retrieve top-K relevant chunks using semantic search
8. Generate final answers using an LLM

---

## Project Structure
AI-Tutor/
│
├── pdf/
│ └── science101.pdf
│
├── chapter1_chunks.json
├── chapter1_texts.json
├── chapter1_index.faiss
│
├── pdf_to_chunks.py
├── build_faiss_index.py
├── ai_tutor_chat.py
│
└── README.md


---

## Installation

Install all required dependencies using pip:

```bash
pip install pymupdf sentence-transformers faiss-cpu numpy requests

API Setup

This project uses OpenRouter API to generate answers.

Replace the API key in the script:

api_key = "YOUR_OPENROUTER_API_KEY"


⚠️ Do not upload your API key to GitHub.

How to Run
Step 1: Extract Text and Create Chunks
python pdf_to_chunks.py

Step 2: Generate Embeddings and FAISS Index
python build_faiss_index.py

Step 3: Start the AI Tutor
python ai_tutor_chat.py

Sample Interaction
Question: What is photosynthesis?

AI Tutor:
Photosynthesis is the process by which green plants make their own food
using sunlight, water, and carbon dioxide.

Key Highlights

Implements Retrieval-Augmented Generation (RAG)

Prevents hallucinations by grounding answers in textbook data

Fast semantic retrieval using FAISS

Easily extendable to multiple chapters and subjects

Suitable for GenAI, NLP, and EdTech portfolios

Future Enhancements

Support for multiple chapters and subjects

Web interface using Streamlit or Gradio

Display source text for each answer

Voice-based question answering

Multi-language support

Author

Chesta Rawat
Data Analyst | GenAI & NLP Enthusiast

License

This project is created for educational and learning purposes.


