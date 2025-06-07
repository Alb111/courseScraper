import requests
from bs4 import BeautifulSoup, Tag, ResultSet

# Get HTML from BSOE course website
URL: str = "https://courses.engineering.ucsc.edu/courses"
page: requests.Response = requests.get(URL)

# Put into a soup object and parse for li
soup: BeautifulSoup = BeautifulSoup(page.content, "html.parser")
course_links: ResultSet = soup.find_all("li")

print(type(course_links[0]))
print(type(course_links))


# print(page.text)
