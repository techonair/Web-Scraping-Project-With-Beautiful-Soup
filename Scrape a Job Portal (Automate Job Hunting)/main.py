import requests
from bs4 import BeautifulSoup

def extract(page):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}
    url = f'https://www.linkedin.com/jobs/search/?geoId=112376381&keywords=python%20developer&location=Bangalore%20Urban%2C%20Karnataka%2C%20India&start={page}'
    r = requests.get(url, headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

def transform(soup):
    divs = soup.find_all('div', class_ = 'job-card-container--clickable')
    
    

c = extract(0)

