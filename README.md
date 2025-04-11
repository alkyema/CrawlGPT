# 🧠 CrawlGPT - Personalized Web Knowledge Chatbot

CrawlGPT is a smart, **LLM-powered personalized assistant** that learns from **websites you provide**. Just give it a URL, and it will:

✅ Scrape the full website and related pages  
✅ Chunk and vectorize the content  
✅ Use **Retrieval-Augmented Generation (RAG)** to power accurate, personalized answers  
✅ Respond with context-aware replies using **Gemini** (or other LLMs)

---

## 🚀 Features

- 🔗 **Website Scraping** – Provide a URL and it fetches full text content across the main site and related links.
- 📚 **Context-Aware Q&A** – Ask anything about the site and get answers based on its actual content.
- 🧠 **RAG Implementation** – Vectorizes content into embeddings and retrieves context for the LLM.
- 🧪 **Gemini-Powered LLM** – Uses Google's Gemini for intelligent, conversational responses.
- 🛠️ **Pluggable Architecture** – Swap LLMs (OpenAI, Local LLMs, Claude, etc.)
- 🗂️ **Supports Multiple Users** – Store and manage personalized website knowledge per user.

---

## 🧰 Tech Stack

| Layer         | Tech Used                         |
|--------------|------------------------------------|
| **LLM**       | Gemini API                         |
| **RAG Engine**| FAISS (Vector DB) + Custom Retriever |
| **Scraper**   | BeautifulSoup, Requests, urllib    |
| **Backend**   | Python (FastAPI / Flask)           |
| **Frontend**  | React.js (optional for UI)         |
| **Embedding** | SentenceTransformers / Gemini Embeddings |

---

## 🧠 How It Works

1. **Input URL** ➝ User provides a URL
2. **Crawl & Scrape** ➝ The website and related links are fetched and cleaned
3. **Chunk & Embed** ➝ Text is broken into chunks and converted into vector embeddings
4. **Store in FAISS** ➝ Indexed for similarity search
5. **Ask Question** ➝ User inputs a query
6. **Retrieve Context** ➝ Top relevant chunks are retrieved from vector DB
7. **LLM Response** ➝ Gemini generates a context-rich answer

---

## 📦 Installation

```bash
git clone https://github.com/yourusername/CrawlGPT.git
cd CrawlGPT
pip install -r requirements.txt
```

---

## ⚙️ .env Example

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

---

## ▶️ Run the App

```bash
python test.py
```

Or with FastAPI:
```bash
uvicorn mainAPI:app --reload --port 8888
```

---

## 📁 Folder Structure

```
CrawlGPT/
│
├── FrontEnd
    ├── ChatBot.html            # Main FrontEnd file                 
├── BackEnd                 
    ├── mainAPI.py              # Main app file
    ├── scraper.py/             # Website scraping logic
    ├── embeddings.py/          # Embedding + FAISS functions
    ├── query_engine.py/        # Gemini API integration
    ├── data/                   # Stores raw/cleaned content
    ├── .env                    # Secrets (not committed)
    ├── requirements.txt        # Python dependencies
```

---

## 🔮 Future Plans

- ✅ Add OpenAI & Claude model support  
- 🌍 Enable multi-site comparison  
- 💾 Add persistent DB (e.g., Qdrant, Pinecone)  
- 🧑‍💻 Build React-based chat interface  
- 🔐 Add user auth & API rate limits

---

## 🧑‍💻 Created By

- **Satwik Kishore**  
> _Built for people who want to teach AI from their own corner of the internet._

---


> 📚 “Your personalized AI librarian — trained on the web you choose.”
