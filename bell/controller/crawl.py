# Request stock information from NASDAQ

import urllib
from bs4 import BeautifulSoup

BASE_URL = 'http://www.nasdaq.com/earnings/report/'

class Crawler:
    def __init__(self):
        pass

    def get_earning_date_items(self, html):
        return BeautifulSoup(html, 'html.parser').find('div', {'class': 'genTable'})('tr')

    def get_row_item(self, html, row_type='th'):
        return [BeautifulSoup(str(html_item), 'html.parser').text
                for html_item in BeautifulSoup(html, 'html.parser')(row_type)]

    def get_row_header(self, html):
        return self.get_row_item(html, 'th')

    def get_row_data(self, html):
        return self.get_row_item(html, 'td')

    def get_symbol_data(self, symbol):
        html = urllib.urlopen(BASE_URL+ symbol).read()
        earnings = self.get_earning_date_items(html)
        results = []
        results.append(self.get_row_header(str(earnings[0])))
        for earning_data in earnings[1:]:
            results.append(self.get_row_data(str(earning_data)))
        print results
