from typing import Iterator, NamedTuple, Tuple
import requests
from bs4 import Tag, ResultSet, BeautifulSoup
from requests.models import stream_decode_response_unicode


# the following fucntions takes string like:
# "CSE101: Data Structure and Algo"
#  and splits it into the code and name
def get_course_name(raw: Tag) -> str:
    inner_txt: str = raw.decode_contents()
    return inner_txt.split(":")[0]


def get_course_code(raw: Tag) -> str:
    inner_txt: str = raw.decode_contents()
    return inner_txt.split(":")[1][1:]

# appends href to root link
def get_link(raw: Tag) -> str:
    page_route: str = str(raw.get("href"))
    return "https://courses.engineering.ucsc.edu" + page_route
    
# fetches coure credits and description
def get_description(link: str) -> tuple[str, str]:
    page: requests.Response = requests.get(link)
    soup = BeautifulSoup(page.content, "html.parser")
    elements = soup.find(id="block-bsoe-specific-content")
    .select("p")
    courseDis: str = elements[0].decode_contents()
    creditNum: str = elements[1].decode_contents()
    return (courseDis, creditNum)

# Name Tuple that iter returns
class Course(NamedTuple):
    code: str
    name: str
    link: str
    course_discription: str
    credit_num: str


# iterator that returns every course as a nameTuple
class Courses(Iterator[Course]):
    def __init__(self, li_tags: ResultSet) -> None:
        self.limit: int = len(li_tags) - 1
        self.current: int = 13
        self.li_tags: ResultSet = li_tags

    def __iter__(self) -> Iterator[Course]:
        return self

    def __next__(self) -> Course:
        if self.current == self.limit:
            raise StopIteration

        tag: Tag = self.li_tags[self.current]
        self.current += 1

        class_code: str = get_course_code(tag)
        class_name: str = get_course_name(tag)
        class_link: str = get_link(tag)
        dis_and_credit: tuple[str,str] = get_description(class_link)
        return Course(class_code, class_name, class_link, dis_and_credit[0], dis_and_credit[1])
