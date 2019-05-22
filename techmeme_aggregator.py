from bs4 import BeautifulSoup
import requests

def techmeme(term):
    try:
        url = 'https://www.techmeme.com/search/query?q={}&wm=false'.format(term)
        source = requests.get(url)
        soup = BeautifulSoup(source.text, 'html.parser')
        container = soup.find('div', class_= 'items')
        all_items = container.find_all('div', class_= 'item')
        techmeme_results = {}
        for item in all_items:
            author_container = item.find('table', class_= 'shrtbl')
            author_link = author_container.a['href']
            author = author_container.text
            heading_container = item.find('strong', class_= 'L2')
            heading_link = heading_container.a['href']
            heading = heading_container.text
            techmeme_results[heading] = {'author_link': author_link, 'author': author, 'heading_link': heading_link}
    
    except AttributeError:
        techmeme_results = None

    return techmeme_results
        