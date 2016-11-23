# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful
# combining from https://github.com/wfdd/inatsisartut-scraper/blob/master/scraper.py 
# AND https://github.com/ianibo/SirsiDynixIBistroScraper/blob/master/scraper.py

import scraperwiki
import lxml.html
import hashlib
import re
from splinter import Browser
import sys, traceback, logging, shutil, platform
from string import ascii_lowercase

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
