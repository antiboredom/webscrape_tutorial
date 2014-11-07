import urllib
from bs4 import BeautifulSoup

url = 'http://www.alibaba.com/catalogs/products/CID100003006'
data = urllib.urlopen(url).read()
soup = BeautifulSoup(data)

for item in soup.select('.item-main'):
    title = item.find('h2').text.strip()

    attributes = item.select('.lwrap .attr')

    if len(attributes) < 2:
        continue

    price = attributes[0].text.strip()
    quantity = attributes[1].text.strip()

    image = item.select('.image img')[0].get('src')
    if image is None:
        image = item.select('.image img')[0].get('image-src')

    print title + ',' + price + ',' + quantity + ',' + image

