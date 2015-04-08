Simple Web Scraping with Python
===============================

### First: Install BeautifulSoup

If you have pip, just run `pip install beautifulsoup4`

Otherwise, [download BeautifulSoup here](http://www.crummy.com/software/BeautifulSoup/bs4/download/4.3/beautifulsoup4-4.3.2.tar.gz), then extract the file and move the `bs4` to wherever you're project is located.

### Python Basics

Create a string:
`activity = 'scraping'`

Create an integer:
`year = 2014`

Arrays (in python, called lists):
`some_numbers = [1, 2, 3, 4, 5]`

Functions
```
def say_hello(name):
  print 'hello ' + name
```

### Examples

#### Get the contents of a web page
```
import urllib

url = 'http://alibaba.com/catalogs/products/CID100003006'
data = urllib.urlopen(start_url).read()
print data
```

#### Print the text of all the links in a web page
```
import urllib
from bs4 import BeautifulSoup

url = 'http://alibaba.com/catalogs/products/CID100003006'
data = urllib.urlopen(url).read()
soup = BeautifulSoup(data)

for link in soup.select('a'):
    print link.text.strip()

```

### Resources
* [Learn Python The Hard Way](http://learnpythonthehardway.org/book/)
* [Python Docs](https://docs.python.org/2.7/)
* [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [CSS Selectors](http://www.w3schools.com/cssref/css_selectors.asp)
* [Scrapy](http://scrapy.org/)
* [Casper](http://casperjs.org/)
