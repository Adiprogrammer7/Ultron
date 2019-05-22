import requests
from bs4 import BeautifulSoup

def verge():
    source = requests.get("https://www.theverge.com/").text
    soup = BeautifulSoup(source, 'html.parser')
    result_container = soup.find('div', class_ = 'c-compact-river')
    all_headings = result_container.find_all('h2', class_= 'c-entry-box--compact__title')
    verge_results = {}
    for heading in all_headings:
        verge_results[heading.text] = heading.a['href']
    
    return verge_results

def techcrunch():
    source = requests.get("https://techcrunch.com/").text
    soup = BeautifulSoup(source, 'html.parser')
    headings = soup.find_all('h2', class_= 'post-block__title')
    techcrunch_results = {}
    for heading in headings:
        techcrunch_results[heading.text.strip()] = heading.a['href']

    return techcrunch_results