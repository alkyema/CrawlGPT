import os
import faiss
import numpy as np
from dotenv import load_dotenv
from tiktoken import get_encoding
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def num_tokens_from_string(string: str, encoding_name="cl100k_base") -> int:
    encoding = get_encoding(encoding_name)
    return len(encoding.encode(string))

def chunk_text(text, max_tokens=500):
    sentences = text.split('. ')
    chunks = []
    current_chunk = ""

    for sentence in sentences:
        if num_tokens_from_string(current_chunk + sentence) <= max_tokens:
            current_chunk += sentence + ". "
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sentence + ". "
    if current_chunk:
        chunks.append(current_chunk.strip())
    return chunks

def get_embedding(text, model_name="models/embedding-001"):
    res = genai.embed_content(model=model_name, content=text, task_type="retrieval_document")
    return res["embedding"]

def process_scraped_data(scraped_data: dict):
    documents = []
    sources = []

    for url, content in scraped_data.items():
        chunks = chunk_text(content)
        for chunk in chunks:
            documents.append(chunk)
            sources.append(url)

    print(f"Total chunks: {len(documents)}")

    dim = 768
    index = faiss.IndexFlatL2(dim)
    vectors = []

    for doc in documents:
        emb = get_embedding(doc)
        vectors.append(np.array(emb).astype("float32"))

    index.add(np.array(vectors))
    
    print(f"Stored {len(vectors)} vectors in FAISS.")
    return index, documents, sources

def query_faiss_index(index, documents, sources, query, k=3):
    query_embedding = get_embedding(query)
    query_vector = np.array(query_embedding).astype("float32").reshape(1, -1)

    distances, indices = index.search(query_vector, k)

    retrieved_chunks = [documents[i] for i in indices[0]]
    context = "\n\n".join(retrieved_chunks)

    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(f"Answer the following question based on the context:\n\n{context}\n\nQuestion: {query}")
    answer = response.text

    best_source = sources[indices[0][0]]
    return answer, best_source
