# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful
# combining from https://github.com/wfdd/inatsisartut-scraper/blob/master/scraper.py 
# AND https://github.com/ianibo/SirsiDynixIBistroScraper/blob/master/scraper.py

from collections import namedtuple
import datetime as dt
import itertools as it
import re
import sqlite3
from urllib.parse import parse_qs, urljoin, urlparse, quote as urlquote

PARSER_ID = 'hanz'

base_url = 'http://www.takealot.com'


def gather_landing_pages(session):
  for toplevel in session.find_by_xpath('//*[@id="nav"]/li/ul/li'):
    name = toplevel.find_by_xpath('a/span[1]')
    url = toplevel.find_by_xpath('a')['href']
    print name + ',' + url


def main():
    with Browser('phantomjs', load_images=False) as browser:
        browser.visit(base_url)
        landing_pages = list(gather_landing_pages(browser))
        
        # a bunch of stuff excluded for now
        
  
if __name__ == '__main__':
    main()
