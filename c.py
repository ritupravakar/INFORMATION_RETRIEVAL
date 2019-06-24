import re
import http.client
import urllib
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import urllib.request

regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

def isValidUrl(url):
    if regex.match(url) is not None:
        return True;
    return False

def crawler(SeedUrl):
    tocrawl=[SeedUrl]
    crawled=[]
    while tocrawl:
        page=tocrawl.pop()
        print('Crawled:'+page)
        pagesource=urllib.request.urlopen(page)
        s=pagesource.read()
        print(s)
        soup=BeautifulSoup(s,features="html.parser")
        links=soup.findAll('a',href=True)
        if page not in crawled:
            for l in links:
                if isValidUrl(l['href']):
                    tocrawl.append(l['href'])
            crawled.append(page)
    return crawled
crawler('https://www.google.com/')
