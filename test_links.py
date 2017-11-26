from concurrent.futures import ThreadPoolExecutor
from html.parser import HTMLParser
from subprocess import check_call
from urllib.error import URLError
from urllib.request import urlopen


class LinksParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            attrs = dict(attrs)
            attrs['lineno'] = self.getpos()[0]
            self.links.append(attrs)


def check_link(link):
    try:
        urlopen(link['href'])
        return True
    except URLError:
        return False


def test_links():
    check_call(['make'])
    lp = LinksParser()
    with open('cheatsheet.html') as fp:
        lp.feed(fp.read())

    with ThreadPoolExecutor(max_workers=min(100, len(lp.links))) as pool:
        results = zip(lp.links, pool.map(check_link, lp.links))

    errors = [result for result in results if not result[1]]
    assert not errors, errors
