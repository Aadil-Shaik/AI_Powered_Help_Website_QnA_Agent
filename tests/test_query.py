import unittest
import sys
import os
import numpy as np
from sentence_transformers import SentenceTransformer

# Ensure 'src' is in sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from query import search_documents, answer_query

# Load the real model to generate embeddings of correct shape (384-d)
model = SentenceTransformer('all-MiniLM-L6-v2')

# Sample mock index with correct embedding shape
mock_index = [
    {'url': 'https://help.example.com/page1', 'text': 'How to create a Slack channel: Click the "+" icon.', 'embedding': model.encode("How to create a Slack channel.")},
    {'url': 'https://help.example.com/page2', 'text': 'Slack troubleshooting tips: Check your internet connection.', 'embedding': model.encode("Slack troubleshooting tips.")},
]

class TestQueryProcessing(unittest.TestCase):
    def test_search_documents(self):
        """Test if search retrieves the correct document"""
        query = "create a Slack channel"

        # Run search
        results = search_documents(query, mock_index, top_k=1, similarity_threshold=0.1)
        self.assertTrue(len(results) > 0)
        self.assertIn("create a Slack channel", results[0]['text'])

    def test_answer_query(self):
        """Test if answer_query correctly retrieves an answer"""
        query = "How do I create a Slack channel?"
        answer = answer_query(query, mock_index)
        
        # Allow flexible matching (not strict on exact wording)
        self.assertTrue("click the \"+\" icon" in answer.lower() or "To create a Slack channel" in answer)

if __name__ == '__main__':
    unittest.main()
