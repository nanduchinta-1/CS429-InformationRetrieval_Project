from flask import Flask, request, jsonify
import pickle
from processor import query_processor

# Load inverted index, TF-IDF matrix, and file paths
with open('inverted_index.pkl', 'rb') as f:
    inverted_index = pickle.load(f)

with open('tfidf_matrix.pkl', 'rb') as f:
    tfidf_matrix = pickle.load(f)

with open('file_paths.pkl', 'rb') as f:
    file_paths = pickle.load(f)

app = Flask(__name__)

@app.route('/query', methods=['POST'])
def query():
    data = request.json
    query = data.get('query')
    k = data.get('k')  # Default to None if k is not provided

    if not query:
        return {"error": "Query is required"}, 400

    if k is not None:
        if not isinstance(k, int) or k <= 0:
            return {"error": "k should be a positive integer"}, 400

    results = query_processor(query, inverted_index, tfidf_matrix, file_paths, k)

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)