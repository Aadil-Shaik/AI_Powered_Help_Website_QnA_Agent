import argparse
import time
from crawler import crawl_website
from processor import process_content, build_index
from query import answer_query

def main():
    parser = argparse.ArgumentParser(description="AI-powered Q&A Agent")
    parser.add_argument('--url', required=True, help='Help website URL')
    args = parser.parse_args()

    print("Crawling website...")
    start_time = time.time()
    pages = crawl_website(args.url)
    crawl_time = time.time() - start_time
    print(f"Crawled {len(pages)} pages in {crawl_time:.2f} seconds.")

    if not pages:
        print("No pages found. Exiting.")
        return

    print("Processing content...")
    start_time = time.time()
    documents = process_content(pages)
    process_time = time.time() - start_time
    print(f"Processed {len(documents)} document chunks in {process_time:.2f} seconds.")

    print("Building index...")
    start_time = time.time()
    index = build_index(documents)
    index_time = time.time() - start_time
    print(f"Built index with {len(index)} entries in {index_time:.2f} seconds.")

    print("Agent is ready! Type a question (type 'exit' to quit):")
    while True:
        user_input = input("> ")
        if user_input.lower() in ['exit', 'quit']:
            break
        start_time = time.time()
        answer = answer_query(user_input, index)
        response_time = time.time() - start_time
        print(answer)
        print(f"Response generated in {response_time:.2f} seconds.")

if __name__ == "__main__":
    main()
