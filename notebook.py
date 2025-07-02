import fitz  # PyMuPDF
import json

# Load the PDF
doc = fitz.open(r"C:\Users\hp\Documents\GitHub\AI Tutor\pdf\science101.pdf")

# Extract and clean text from each page
all_text = ""
for page in doc:
    text = page.get_text()
    if text:
        all_text += text + "\n"

doc.close()

# Split into chunks - here, by paragraph (double newline)
raw_chunks = [chunk.strip() for chunk in all_text.split("\n\n") if chunk.strip()]

# Save as JSON
data = [{"id": i, "text": chunk} for i, chunk in enumerate(raw_chunks)]

with open("chapter1_chunks.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ Done. Total chunks: {len(data)}")
import json

with open("chapter1_chunks.json", "r", encoding="utf-8") as f:
    data = json.load(f)

texts = [item["text"] for item in data]

from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(texts, show_progress_bar=True)

import faiss
import numpy as np

dimension = embeddings[0].shape[0]  # 384 for MiniLM
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))

# Optional: Save FAISS index and text data for later use
faiss.write_index(index, "chapter1_index.faiss")

with open("chapter1_texts.json", "w", encoding="utf-8") as f:
    json.dump(texts, f, ensure_ascii=False, indent=2)

print(f"✅ Indexed {len(texts)} chunks in FAISS.")
from sentence_transformers import SentenceTransformer
import numpy as np
import faiss
import json
import requests

# Load the embedding model and FAISS index
print("🔄 Loading model and textbook data...")
model_embed = SentenceTransformer("all-MiniLM-L6-v2")
index = faiss.read_index("chapter1_index.faiss")

with open("chapter1_chunks.json", "r", encoding="utf-8") as f:
    chunks_data = json.load(f)
    chunk_texts = [item["text"] for item in chunks_data]

print("✅ AI Tutor is ready. Ask anything from Chapter 1 (Science Class 8)")

# OpenRouter API setup
api_key = "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"  # Replace with your actual key
headers = {
    "Authorization": f"Bearer {api_key}",
    "HTTP-Referer": "https://openrouter.ai",
    "X-Title": "ai-tutor"
}

# Start the question-answer loop
while True:
    user_question = input("\n🧑‍🎓 Question (or type 'exit'): ").strip()

    if user_question.lower() == "exit":
        print("👋 Goodbye! Keep learning.")
        break

    # Embed the user question
    q_embed = model_embed.encode([user_question])
    top_k = 3
    _, indices = index.search(np.array(q_embed), top_k)
    retrieved_chunks = "\n\n".join([chunk_texts[i] for i in indices[0]])

    # Final clean prompt
    prompt = f"""
You are an AI tutor for 8th-grade students.

Answer the student's question based ONLY on the textbook content provided below.

Use simple, clear language. Do NOT copy full paragraphs.
If the answer is not present, say: "Sorry, I couldn't find the answer in the textbook."

---
Textbook:
{retrieved_chunks}

Question: {user_question}
Answer:
"""

    payload = {
    "model": "anthropic/claude-3-haiku",  # 👈 working alternative
    "messages": [{"role": "user", "content": prompt}]
}


    try:
        response = requests.post("https://openrouter.ai/api/v1/chat/completions",
                                 headers=headers, json=payload)
        response_json = response.json()

        if "choices" in response_json:
            answer = response_json["choices"][0]["message"]["content"]
            print(f"\n🤖 AI Tutor: {answer}")
        else:
            error_msg = response_json.get("error", {}).get("message", "Unknown error")
            print(f"\n❌ API Error: {error_msg}")

    except Exception as e:
        print("\n❌ Request failed:")
        print(e)
