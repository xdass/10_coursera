import requests
import bs4
import openpyxl
from lxml import etree

HEADER_FOR_RU = {'accept-language': 'ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4'}


def get_courses_url_list():
    result = requests.get('https://www.coursera.org/sitemap~www~courses.xml')
    tree = etree.fromstring(result.content)
    courses_links = [node[0].text for node in tree]
    return courses_links[:20]


def get_course_info(course_url):
    r = requests.get(course_url, headers=HEADER_FOR_RU)
    soup = bs4.BeautifulSoup(r.content, 'lxml')
    course_title = soup.select_one('.title').string
    course_start_date = soup.select_one('.startdate span').string
    course_language = soup.select_one('.rc-Language').text
    course_rating = soup.select_one('.ratings-info div:nth-of-type(2)')
    if course_rating:
        course_rating = course_rating.string
    course_weeks = len(soup.select('.rc-WeekView > div'))
    return {
        course_title,
        course_start_date,
        course_language,
        course_rating,
        course_weeks
    }


def collect_courses_info():
    pass


def output_courses_info_to_xlsx(filepath):
    pass


if __name__ == '__main__':
    courses_links = get_courses_url_list()
    get_course_info(courses_links[1])
