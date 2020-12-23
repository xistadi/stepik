import re
import urllib.request

a = input()
b = input()

def get_links(url):
    try:
        fp = urllib.request.urlopen(url)
        mybytes = fp.read()
        mystr = mybytes.decode("utf8")
        fp.close()
        links = re.findall(r'<a.*href="([^"]*)"', mystr)
    except:
        return []
    else:
        return links

def two_steps():
    links1 = get_links(a)

    for link in links1:
        links2 = get_links(link)
        if b in links2:
            return True
    return False

if two_steps():
    print("Yes")
else:
    print("No")