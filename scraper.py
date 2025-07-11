import requests
import courses
from bs4 import BeautifulSoup, ResultSet

# Get HTML from BSOE course website
URL: str = "https://courses.engineering.ucsc.edu/courses"
page: requests.Response = requests.get(URL)

# Put into a soup object and parse for li
soup: BeautifulSoup = BeautifulSoup(page.content, "html.parser")

course_links: ResultSet = soup.select("li > a")  # Select all <a> directly inside <li>

BSOEcourses: courses.Courses = courses.Courses(course_links)
for course in BSOEcourses:
    print(f"Code: {course.code}")
    print(f"Name: {course.name}")
    print(f"Link: {course.link}")
    print(f"Description: {course.course_discription}")
    print(f"Credit Number: {course.credit_num}")
    print("------")
    break
