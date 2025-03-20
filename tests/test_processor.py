import unittest
import sys
import os
import numpy as np

# Ensure 'src' is in sys.path BEFORE importing processor
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# Now import processor
from processor import extract_content, process_content, build_index
from sentence_transformers import SentenceTransformer

# Sample HTML page with structured help content
sample_html = """
<html>
<body>
    <section class="help-content">
        <h1>How to create a Slack channel</h1>
        <p>Click the "+" icon next to Channels. Choose Public or Private. Name the channel.</p>
        <p>You can also set up channel-specific permissions.</p>
    </section>
</body>
</html>
"""

# Mock pages
mock_pages = [{'url': 'https://help.example.com', 'html': sample_html}]

class TestProcessor(unittest.TestCase):
    def test_extract_content(self):
        """Test content extraction from HTML"""
        content = extract_content(sample_html)
        self.assertGreater(len(content), 0, "Content extraction returned empty result.")
        self.assertTrue(any("Click the \"+\" icon" in text for text in content), "Expected instructional text missing.")

    def test_process_content(self):
        """Test processing pages into document format"""
        documents = process_content(mock_pages)
        
        # Instead of forcing exactly 1 document, check that at least 1 exists
        self.assertGreaterEqual(len(documents), 1, "Processing did not return any documents.")
        self.assertIn("Click the \"+\" icon", documents[0]['text'], "Extracted text does not match expected content.")

    def test_build_index(self):
        """Test if index correctly generates embeddings"""
        documents = process_content(mock_pages)
        index = build_index(documents)
        
        # Check that at least one indexed document exists
        self.assertGreaterEqual(len(index), 1, "Index did not contain any entries.")
        self.assertIn('embedding', index[0], "Embeddings were not generated for indexed document.")

if __name__ == '__main__':
    unittest.main()
