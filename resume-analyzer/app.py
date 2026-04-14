import os
from dotenv import load_dotenv
from docx import Document
import numpy as np
import faiss
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def load_resume(file_path):
    doc = Document(file_path)
    text = ""
    for para in doc.paragraphs:
        text += para.text + "\n"
    return text

def chunk_text(text, chunk_size=300):
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size):
        chunks.append(" ".join(words[i:i + chunk_size]))
    return chunks

def get_embeddings(texts):
    embeddings = []
    for text in texts:
        response = client.embeddings.create(
            model="text-embedding-3-small",
            input=text
        )
        embeddings.append(response.data[0].embedding)
    return np.array(embeddings).astype("float32")

def create_vector_store(embeddings):
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    return index

def ask_question(query, chunks, index, k=3):
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=query
    )

    query_vector = np.array([response.data[0].embedding]).astype("float32")
    distances, indices = index.search(query_vector, k)

    relevant_chunks = [chunks[i] for i in indices[0]]
    context = "\n\n".join(relevant_chunks)

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You answer questions about a resume."},
            {"role": "user", "content": "Resume:\n\n" + context + "\n\nQuestion: " + query}
        ]
    )

    return completion.choices[0].message.content

def main():
    print("Loading resume...")
    resume_text = load_resume("anjan_resume.docx")

    print("Chunking...")
    chunks = chunk_text(resume_text)

    print("Embedding...")
    embeddings = get_embeddings(chunks)

    print("Building index...")
    index = create_vector_store(embeddings)

    print("Ready! Ask questions (type 'exit' to quit)\n")

    while True:
        query = input("Question: ")
        if query.lower() == "exit":
            break

        answer = ask_question(query, chunks, index)
        print("\nAnswer:\n" + answer + "\n")

if __name__ == "__main__":
    main()