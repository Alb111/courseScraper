import requests
from bs4 import BeautifulSoup

URL: str = "https://pisa.ucsc.edu/class_search/"
page: requests.Response = requests.get(URL)

# soup: BeautifulSoup = BeautifulSoup(page.content, "html.parser")
print(page.text)
