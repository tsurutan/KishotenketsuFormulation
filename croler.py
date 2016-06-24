# coding:utf-8

import json
import urllib2
from urlparse import urljoin
from BeautifulSoup import *


def crawl(pages, depth=2):
    setpages = set()

    for i in range(depth):
        newpages = set()
        for page in pages:
            try:
                c = urllib2.urlopen(page)
            except:
                print "Could not open %s" % page
                continue
            soup = BeautifulSoup(c.read())
            setpages.add(page)

            links = soup('a')
            for link in links:
                if ('href' in dict(link.attrs)):
                    url = urljoin(page, link['href'])
                    if url.find("'") != -1: continue
                    url = url.split('#')[0]
                    if url[0:4] == 'http' and not url in setpages:
                        newpages.add(url)
        pages = newpages

    return list(setpages)


if __name__ == "__main__":
    urls = ["http://news.yahoo.co.jp/"]

    pages = crawl(urls)

    f = open("./urls.json", "w")
    json.dump(pages, f)
    f.close()
