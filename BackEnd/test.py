from scraper import scrape_website
from embed_store import process_scraped_data
from query_engine import answer_query


urls = [
    "http://13.60.45.204/Protfolio.html",
    "http://13.60.45.204/Neeharikaprotfolio.html",
    "https://apexiq.ai/blog/4a4ea474-dd18-45a4-880e-a862cc5181c1"
]

all_scraped = {}
for url in urls:
    scraped = scrape_website(url)
    all_scraped.update(scraped)

index, documents, sources = process_scraped_data(all_scraped)

while True:
    query = input("\nYou: ")
    if query.lower() == "exit":
        break
    response = answer_query(query, index, documents, sources)
    print(f"\n🤖 BOT: {response}")
