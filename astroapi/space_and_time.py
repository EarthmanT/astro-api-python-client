
import calendar
from requests import get
from datetime import datetime
from time import gmtime, strftime


class SpaceAndTime(object):

    def __init__(self):
        now = datetime.now()
        self._day = now.day
        self._month = now.month
        self._year = now.year
        self._hour = now.hour
        self._minute = now.minute
        self._latitude, self._longitude = self.get_current_location()
        self._timezone = self.get_time_zone()

    @property
    def calendar(self):
        return self.get_calendar()

    @property
    def html_calendar(self):
        return self.get_html_calendar()

    @property
    def to_list(self):
        return (self._day,
                self._month,
                self._year,
                self._hour,
                self._minute,
                self._latitude,
                self._longitude,
                self._timezone)

    @staticmethod
    def get_time_zone():
        timezone = strftime("%z", gmtime())
        return timezone.lstrip()[1:].strip('0')

    @staticmethod
    def get_current_location():
        resp = get('http://ipinfo.io/loc')
        coords = resp.text.rstrip().split(',')
        return coords[0], coords[1]

    def get_calendar(self, year=None, month=None, weekday=None):
        year = year or self._year
        month = month or self._month
        weekday = weekday or calendar.SUNDAY
        text_calendar = calendar.TextCalendar(weekday)
        month = text_calendar.formatmonth(year, month)
        return month

    def get_html_calendar(self, year=None, month=None, weekday=None):
        year = year or self._year
        month = month or self._month
        weekday = weekday or calendar.SUNDAY
        text_calendar = calendar.HTMLCalendar(weekday)
        month = text_calendar.formatmonth(year, month)
        return month

