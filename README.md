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

