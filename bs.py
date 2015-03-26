# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import urllib.request

html_doc = """
<html><head><title>The Dormouse's story</title></head>

<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

html_doc = urllib.request.urlopen('http://it-ebooks.info/book/4675/').read()
#print(html_doc.decode('utf-8'))
soup = BeautifulSoup(html_doc.decode('utf-8'))#.encode('utf-8'))

print(soup.prettify())
