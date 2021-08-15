import requests
from bs4 import BeautifulSoup as bs

def wp(num):
    url = 'https://www.washingtonpost.com/world/middle-east/'

    response = requests.get(url=url, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'})
    soup = bs(response.content, 'html.parser')

    soup = (soup.find_all('a', hreflang=True, itemprop=True))

    return [soup[num].text, soup[num]['href']]
  
