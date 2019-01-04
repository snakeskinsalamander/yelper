
'https://www.yelp.com/search?find_desc=dentist&find_loc=San+Francisco%2C+CA&ns=1'
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup

import warnings
import re


class yelper:
    def __init__(self):
        options = Options()
        options.headless = True
        self.version = 'dev-1.0.0'
        self.driver = webdriver.Firefox(options=options)
        self.search_str = ''
    
    def get_info(self):
        find_me = re.sub('\s', r'%2C', input('Find: '))
        in_loc = re.sub('\s', r'%2C', input('From: '))
        self.search_str = 'https://www.yelp.com/search?find_desc={}&find_loc={}%2C+CA&ns=1'.format(find_me, in_loc)

    def parse(self):
        self.driver.get(self.search_str)
        self.driver.implicitly_wait(5)

        self.response = BeautifulSoup(self.driver.page_source, 'html.parser')

        print('-------------------------------------------------')
        # Parse NAme, Telephone and Address
        for item in self.response.find_all('div', {'class': 'lemon--div__373c0__6Tkil arrange__373c0__UHqhV border-color--default__373c0__2oFDT'}):
            for sub in item.find_all('div',{'class': 'lemon--div__373c0__6Tkil largerScrollablePhotos__373c0__3FEIJ arrange__373c0__UHqhV border-color--default__373c0__2oFDT'}):
                element = sub.find('h3', {'class': 'lemon--h3__373c0__5Q5tF heading--h3__373c0__1n4Of alternate__373c0__1uacp'})
                print('Name: {}'.format(element.a.text))

                try:
                    element = sub.find('div', {'class': 'lemon--div__373c0__6Tkil display--inline-block__373c0__2de_K border-color--default__373c0__2oFDT'})
                    print('Phone: {}'.format(element.text))
                except AttributeError as ae:
                    print('Phone: No Contact Info')

                try:
                    element1 = sub.find('address')
                    print('Address1: {}'.format(element1.div.span.text))
                except AttributeError as ae:
                    print('Address: None')

                try:
                    element1 = sub.find('div', {'class': 'lemon--div__373c0__6Tkil u-space-t1 border-color--default__373c0__2oFDT'})
                    print('Address2: {}'.format(element1.div.text))
                except AttributeError as ae:
                    print('Address: None')

                print('-------------------------------------------------')

    def parse2(self):
        self.driver.get(self.search_str)
        self.driver.implicitly_wait(5)

        self.response = BeautifulSoup(self.driver.page_source, 'html.parser')

        print('-------------------------------------------------')
        # Parse NAme, Telephone and Address
        for item in self.response.find_all('div', {'class': 'lemon--div__373c0__6Tkil arrange__373c0__UHqhV border-color--default__373c0__2oFDT'}):
            print(item)

if __name__ == '__main__':

    y = yelper()

    print('Yelper - A Python module for parsing something from https://www.yelp.com')
    print ('Version: {}\n'.format(y.version))
    
    y.get_info()
    print(y.search_str)
    y.parse()

