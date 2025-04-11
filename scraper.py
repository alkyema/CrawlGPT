import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import tldextract

visited = set()

extractor = tldextract.TLDExtract(cache_dir=None)

def is_internal_link(base_url, link):
    base_domain = extractor(base_url).registered_domain
    link_domain = extractor(link).registered_domain
    return base_domain == link_domain

def clean_text(soup):
    
    for tag in soup(['script', 'style', 'header', 'footer', 'nav', 'noscript']):
        tag.decompose()
    text = soup.get_text(separator=' ', strip=True)
    return text

def scrape_website(url, max_pages=30):
    base_url = url
    content_data = {}
    to_visit = [url]

    while to_visit and len(visited) < max_pages:
        current_url = to_visit.pop(0)

        if current_url in visited:
            continue

        try:
            response = requests.get(current_url, timeout=10)
            if response.status_code != 200:
                continue

            soup = BeautifulSoup(response.text, 'html.parser')
            text = clean_text(soup)
            content_data[current_url] = text
            visited.add(current_url)

            for link in soup.find_all('a', href=True):
                full_url = urljoin(base_url, link['href'])
                parsed = urlparse(full_url)

                if is_internal_link(base_url, full_url) and full_url not in visited and parsed.scheme in ['http', 'https']:
                    to_visit.append(full_url)

        except Exception as e:
            print(f"Failed to scrape {current_url}: {e}")

    return content_data


if __name__ == "__main__":
    site_url = "https://apexiq.ai/blog/4a4ea474-dd18-45a4-880e-a862cc5181c1"
    data = scrape_website(site_url)

    for url, content in data.items():
        print(f"\n--- Content from {url} ---\n")
        print(content) 
