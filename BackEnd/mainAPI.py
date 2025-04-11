from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from scraper import scrape_website
from embed_store import process_scraped_data
from query_engine import answer_query

app = FastAPI()
urls = []
index, documents, sources = None, None, None
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/cameranotification")
def read_root():
    return {"notification": "true"}

class toogle(BaseModel):
    url: list

@app.post("/geturl")
def geturl(toogle: toogle, request: Request):
    print(toogle.url)
    clear_data()
    global urls
    urls = toogle.url
    scrape_all_urls()
    return "🤖 done"

def clear_data():
    global urls, index, documents, sources
    urls = []
    index = documents = sources = None
    print({"status": "All data cleared successfully."})

def scrape_all_urls():
    all_scraped = {}
    global urls, index, documents, sources
    for url in urls:
        scraped = scrape_website(url)
        all_scraped.update(scraped)

    index, documents, sources = process_scraped_data(all_scraped)

class conv(BaseModel):
    query: str

@app.post("/generate")
def generate(conv: conv, request: Request):
    print(conv.query)
    response = answer_query(conv.query, index, documents, sources)
    print(f"\n🤖 BOT: {response}")
    return f"🤖 BOT: {response}"