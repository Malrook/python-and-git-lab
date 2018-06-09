#!/usr/bin/python2.7
import urllib2
from bs4 import BeautifulSoup

try:
    # specify the url
    quote_page = 'http://example.com'

    page = urllib2.urlopen(quote_page)

    # parse the html using beautiful soup and store in variable `soup`
    soup = BeautifulSoup(page, 'html.parser')

    # Take out the <p> of name and get its value
    name_box = soup.find('p')
    print name_box.text.strip()

    f = open('example.txt', 'w')
    f.write(name_box.text.strip())
    f.close()
except urllib2.URLError as e:
    print e