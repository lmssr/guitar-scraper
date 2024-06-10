import requests
from bs4 import BeautifulSoup

def scrape_leboncoin():
    url = 'https://www.leboncoin.fr/recherche/?category=41&text=guitare%20électrique%20gaucher'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    guitars = []
    for ad in soup.find_all('li', class_='react-card'):
        title = ad.find('span', class_='ad-card__title').get_text(strip=True)
        price = ad.find('span', class_='ad-card__price').get_text(strip=True)
        link = ad.find('a', class_='ad-card__link')['href']
        guitars.append({'title': title, 'price': price, 'link': link})
    
    return guitars

def scrape_reverb():
    url = 'https://reverb.com/marketplace?query=left-handed%20electric%20guitar'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    guitars = []
    for ad in soup.find_all('div', class_='card--listing'):
        title = ad.find('h4', class_='card-title').get_text(strip=True)
        price = ad.find('span', class_='price').get_text(strip=True)
        link = 'https://reverb.com' + ad.find('a', class_='thumbnail')['href']
        guitars.append({'title': title, 'price': price, 'link': link})
    
    return guitars
