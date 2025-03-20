import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import time
import random
from collections import deque

def normalize_url(url):
    """Normalize URL by removing query parameters and fragments."""
    parsed = urlparse(url)
    return f"{parsed.scheme}://{parsed.netloc}{parsed.path}"

def is_relevant_url(url, start_netloc):
    """Allow all internal links to documentation subpages."""
    parsed = urlparse(url)
    return parsed.netloc == start_netloc  # Only allow links within the same domain

def crawl_website(start_url, max_pages=50, max_depth=3):
    visited = set()
    pages = []
    start_netloc = urlparse(start_url).netloc
    to_visit = deque([(start_url, 0)])

    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml'
    })

    while to_visit and len(pages) < max_pages:
        url, depth = to_visit.popleft()
        normalized_url = normalize_url(url)
        if normalized_url in visited:
            continue

        visited.add(normalized_url)

        try:
            time.sleep(random.uniform(0.5, 1.0))
            response = session.get(url, timeout=10)
            if response.status_code != 200:
                continue

            html = response.text
            if len(html) < 500:  # Ignore short pages
                continue

            pages.append({'url': url, 'html': html})

            if depth < max_depth:
                soup = BeautifulSoup(html, "html.parser")

                # Extract priority links from navigation sections
                nav_links = []
                for nav in soup.select('nav, header, .nav, .menu'):
                    nav_links.extend(nav.find_all("a", href=True))

                all_links = soup.find_all("a", href=True)
                links_to_follow = nav_links + all_links  # Prioritize nav links

                for link in links_to_follow:
                    new_url = urljoin(url, link['href'])
                    new_normalized = normalize_url(new_url)
                    if new_normalized not in visited and is_relevant_url(new_normalized, start_netloc):
                        to_visit.append((new_normalized, depth + 1))

        except Exception as e:
            print(f"Error crawling {url}: {e}")

    return pages
