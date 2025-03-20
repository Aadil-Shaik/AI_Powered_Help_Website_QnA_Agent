from bs4 import BeautifulSoup
from sentence_transformers import SentenceTransformer
import numpy as np

# Load the Sentence Transformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

def extract_content(html):
    """Extract structured documentation content while filtering out non-informative sections."""
    soup = BeautifulSoup(html, "html.parser")

    # Prioritize structured content
    content_sections = []
    for selector in ["article", "section", ".help-content", ".docs-content", ".tutorial", ".guide", ".how-to"]:
        sections = soup.select(selector)
        for section in sections:
            text = section.get_text(separator="\n").strip()
            # Ignore short sections that might be listings
            if len(text) > 100 and "Featured articles" not in text:
                content_sections.append(text)

    # Fallback: Extract paragraphs if no structured content is found
    if not content_sections:
        paragraphs = soup.find_all("p")
        content_sections = [p.get_text(separator="\n").strip() for p in paragraphs if len(p.get_text()) > 100]

    return content_sections if content_sections else []

def process_content(pages):
    """Process pages to extract meaningful content."""
    documents = []
    for page in pages:
        sections = extract_content(page['html'])
        for section in sections:
            if len(section) > 100:
                documents.append({'url': page['url'], 'text': section})

    return documents

def build_index(documents):
    """Build a searchable index with embeddings for retrieved documentation."""
    index = []
    for doc in documents:
        embedding = model.encode(doc['text'])
        index.append({'url': doc['url'], 'text': doc['text'], 'embedding': embedding})
    return index
