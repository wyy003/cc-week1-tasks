import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

titles = soup.select('.titleline > a')

for title in titles:
    print(title.get_text())
