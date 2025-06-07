import requests
from bs4 import BeautifulSoup, ResultSet

# Get HTML from BSOE course website
URL: str = "https://courses.engineering.ucsc.edu/courses"
page: requests.Response = requests.get(URL)

# Put into a soup object and parse for li
soup: BeautifulSoup = BeautifulSoup(page.content, "html.parser")

course_links: ResultSet = soup.select("li > a")  # Select all <a> directly inside <li>

lol = course_links[200].decode_contents()

# print(page.text)
