import numpy as np
from sentence_transformers import SentenceTransformer
from gemini_api import gemini_api_instance

# Load the model
model = SentenceTransformer('all-MiniLM-L6-v2')

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def search_documents(query, index, top_k=5, similarity_threshold=0.30):
    """Retrieve top matching documents based on cosine similarity."""
    query_embedding = model.encode(query)
    results = []
    
    for doc in index:
        score = cosine_similarity(query_embedding, doc['embedding'])
        if score > similarity_threshold:  # Only return relevant results
            results.append({'url': doc['url'], 'text': doc['text'], 'score': score})

    results.sort(key=lambda x: x['score'], reverse=True)
    return results[:top_k]

def answer_query(query, index):
    """Retrieve relevant context and generate answer using Gemini."""
    relevant_docs = search_documents(query, index)
    
    if not relevant_docs:
        return "Sorry, I couldn't find any relevant information in the documentation."

    # Concatenate multiple results to provide more context
    context = "\n".join([doc['text'] for doc in relevant_docs])
    
    return gemini_api_instance.generate_answer(query, context)
