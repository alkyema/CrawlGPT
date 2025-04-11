import numpy as np
import google.generativeai as genai

def search_index(index, query, documents, sources, k=3):
    
    query_embedding = genai.embed_content(
        model="models/embedding-001",
        content=query,
        task_type="retrieval_query"
    )["embedding"]

    D, I = index.search(np.array([query_embedding]).astype("float32"), k)
    
    results = []
    for i in I[0]:
        if i < len(documents):
            results.append((documents[i], sources[i]))
    return results

def answer_query(query, index, documents, sources):
    results = search_index(index, query, documents, sources)
    
    context = "\n\n".join([f"{doc}\n(Source: {src})" for doc, src in results])
    
    prompt = f"""You are a helpful AI assistant. Use the following context to answer the user's question.

Context:
{context}

Question: {query}
Answer:"""

    model = genai.GenerativeModel("models/gemini-1.5-pro")
    response = model.generate_content(prompt)
    return response.text
