import unittest
import sys
import os

# Ensure 'src' is in sys.path BEFORE importing crawler
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# Now import crawler
from crawler import crawl_website

class TestCrawler(unittest.TestCase):
    def test_crawl_website(self):
        """Test basic crawling functionality"""
        url = "https://help.slack.com"
        pages = crawl_website(url, max_pages=2)  # Limit to 2 pages for testing
        
        # Ensure pages are crawled
        self.assertGreater(len(pages), 0, "Crawler did not return any pages.")
        
        # Ensure pages contain valid URLs and HTML content
        for page in pages:
            self.assertIn("html", page['html'].lower(), "Extracted page does not contain valid HTML.")
            self.assertTrue(page['url'].startswith("https://help.slack.com"), "Crawled URL is incorrect.")

if __name__ == '__main__':
    unittest.main()
