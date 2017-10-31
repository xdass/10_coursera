import requests
import bs4
import openpyxl
from lxml import etree


def get_courses_list():
    result = requests.get('https://www.coursera.org/sitemap~www~courses.xml')
    tree = etree.fromstring(result.content)
    # courses_links = [item[0].text for item in tree]


def get_course_info(course_slug):
    pass


def output_courses_info_to_xlsx(filepath):
    pass


if __name__ == '__main__':
    print(get_courses_list())
