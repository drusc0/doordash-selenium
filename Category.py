from enum import Enum


class QueryParam(object):
    def __init__(self):
        self._url_endpoint = '/filters/en-US'
        self._tag = 'cuisine'

    @property
    def tag(self):
        return self._tag

    @property
    def url(self):
        return self._url_endpoint


class Category(Enum):
    BREAKFAST = 'breakfast'
    ASIAN = 'asian'
    THAI = 'thai'
    VEGAN = 'vegan'
    HEALTHY = 'healthy'
    INDIAN = 'indian'
    SUSHI = 'sushi'
    ITALIAN = 'italian'
    MEXICAN = 'mexican'


if __name__ == '__main__':
    for c in Category:
        print(c.name, c.value)
