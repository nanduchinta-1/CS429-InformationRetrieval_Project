import os
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load quotes from txt files
def load_quotes(file_paths):
    quotes = []
    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8') as f:
            quotes.append(f.read())
    return quotes

# Process the quotes and create TF-IDF matrix
def process_quotes(quotes):
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(quotes)
    return vectorizer, tfidf_matrix

# Create inverted index
def create_inverted_index(quotes, vectorizer):
    terms = vectorizer.get_feature_names_out()
    inverted_index = {}
    for idx, term in enumerate(terms):
        inverted_index[term] = [i for i, quote in enumerate(quotes) if term in quote.lower()]
    return inverted_index

# Main function
if __name__ == '__main__':
    # Define file paths
    file_paths = [f'quotes_page_{i}.txt' for i in range(1, 101)]  #Since we have 100 pages
    
    # Load quotes
    quotes = load_quotes(file_paths)
    
    # Process quotes and create TF-IDF matrix
    vectorizer, tfidf_matrix = process_quotes(quotes)
    
    # Create inverted index
    inverted_index = create_inverted_index(quotes, vectorizer)
    
    # Save the objects as pickle files
    with open('inverted_index.pkl', 'wb') as f:
        pickle.dump(inverted_index, f)
        
    with open('tfidf_matrix.pkl', 'wb') as f:
        pickle.dump(tfidf_matrix, f)
        
    with open('file_paths.pkl', 'wb') as f:
        pickle.dump(file_paths, f)
