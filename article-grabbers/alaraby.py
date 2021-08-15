import requests
from bs4 import BeautifulSoup as bs

def alaraby(num):
    tags = []
    url = 'https://english.alaraby.co.uk/'

    response = requests.get(url)

    soup = bs(response.content)

    soup = (soup.find_all('a', href=True, hreflang=True, title=True))

    for i in soup:
        if i.parent.name == 'h2':
            tags.append(i)

    return [
        (tags[num]['title']), # Title 
        (f"https://english.alaraby.co.uk{tags[num]['href']}") # Link
    ]
