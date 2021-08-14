import requests
from bs4 import BeautifulSoup as bs

def aljazeera(num): # Article type1
    url = 'https://www.aljazeera.com/'

    response = requests.get(url)

    soup = bs(response.content, 'html.parser')

    soup = (soup.find_all('a', 'fte-featured__title__link'))

    return [
        ((soup[num]).find('span')), # Title
        (f"https://www.aljazeera.com{soup[num]['href']}") # Link
    ]

def aljazeera2(num): # Article type2
    url = 'https://www.aljazeera.com/'

    response = requests.get(url)

    soup = bs(response.content, 'html.parser')

    soup = (soup.find_all('a', 'fte-featured__excerpt__link fte-featured__title__link'))

    return [
        ((soup[num]).find('p')), # Title
        (f"https://www.aljazeera.com{soup[num]['href']}") # Link
    ]
