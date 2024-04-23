import unittest
from processor import query_processor 
import pickle
import numpy as np

class TestQueryProcessor(unittest.TestCase):

    def setUp(self):
        # Load test data: inverted_index, tfidf_matrix, and file_paths
        with open('inverted_index.pkl', 'rb') as f:
            self.inverted_index = pickle.load(f)

        with open('tfidf_matrix.pkl', 'rb') as f:
            self.tfidf_matrix = pickle.load(f)

        with open('file_paths.pkl', 'rb') as f:
            self.file_paths = pickle.load(f)

    def test_query_processor_with_k(self):
        query = "happy"
        k = 2

        result = query_processor(query, self.inverted_index, self.tfidf_matrix, self.file_paths, k)

        self.assertTrue("results" in result)
        self.assertEqual(len(result["results"]), k)

        # Check if scores are sorted in descending order
        scores = [res["score"] for res in result["results"]]
        self.assertTrue(all(scores[i] >= scores[i + 1] for i in range(len(scores) - 1)))

    def test_query_processor_without_k(self):
        query = "life"

        result = query_processor(query, self.inverted_index, self.tfidf_matrix, self.file_paths)

        self.assertTrue("results" in result)

        # Check if scores are sorted in descending order
        scores = [res["score"] for res in result["results"]]
        self.assertTrue(all(scores[i] >= scores[i + 1] for i in range(len(scores) - 1)))

if __name__ == '__main__':
    unittest.main()
