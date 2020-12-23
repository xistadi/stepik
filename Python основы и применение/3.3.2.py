import re
import urllib.request
from urllib.parse import urlparse

url = input()


def get_links():
    try:
        fp = urllib.request.urlopen(url)
        mybytes = fp.read()
        mystr = mybytes.decode("utf8")
        fp.close()
        links = re.findall(r'<a.+href=[\'"]([^./][^\'"]*)[\'"]', mystr)
    except:
        return []
    else:
        return links


def parse_link(link):
    parsed_uri = urlparse(link)
    res = parsed_uri.netloc
    try:
        return res[:res.index(':')]
    except:
        return res
    else:
        return res[:res.index(':')]


links = get_links()

unsorted = list(map(parse_link, links))

for link in sorted(list(set(unsorted))):
    print(link)