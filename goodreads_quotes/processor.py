from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def query_processor(query, inverted_index, tfidf_matrix, file_paths):
    # Split the query into terms
    terms = query.lower().split()

    # Validate and error-check the terms
    for term in terms:
        if term not in inverted_index:
            return {"error": f"Term '{term}' not found in the index"}, 400

    # Create a TF-IDF vectorizer using the vocabulary from the inverted index
    vectorizer = TfidfVectorizer(stop_words='english', vocabulary=inverted_index.keys())

    # Calculate query TF-IDF vector
    query_tfidf = vectorizer.fit_transform([query])

    # Calculate cosine similarity between query and documents
    cosine_similarities = cosine_similarity(query_tfidf, tfidf_matrix).flatten()

    # Get top ranked documents
    top_indices = cosine_similarities.argsort()[::-1]

    results = []
    for idx in top_indices:
        file_path = file_paths[idx]
        results.append({
            "file_path": file_path,
            "score": cosine_similarities[idx]
        })

    return {"results": results}