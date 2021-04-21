
from bs4 import BeautifulSoup


def soupify_calendar(html_calendar):
    return BeautifulSoup(html_calendar, 'html.parser')


def add_formatting_to_date(html_calendar):
	# TODO Add formatting to date
    pass
