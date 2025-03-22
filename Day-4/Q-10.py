from bs4 import BeautifulSoup
import requests
from concurrent.futures import ThreadPoolExecutor

def retrieve(url):
    response = requests.get(url)
    return response.text

def extract_links(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    return [anchor.get('href') for anchor in soup.find_all('a', href=True)]

def fetch_and_extract(url):
    content = retrieve(url)
    links = extract_links(content)
    print(links)

if __name__ == '__main__':
    target_url = "https://docs.python.org/3/"
    with ThreadPoolExecutor(max_workers=5) as executor:
        tasks = [executor.submit(fetch_and_extract, target_url) for _ in range(5)]
    for task in tasks:
        task.result()