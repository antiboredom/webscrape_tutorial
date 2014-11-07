import urllib
import json
import time
import json
from bs4 import BeautifulSoup

base_url = 'http://www.alibaba.com/'
start_url = base_url + 'catalogs/products/CID100003006----------------------50'

output = []

def download_image(url):
    if url is None:
        return False

    print 'downloading', url
    img_filename = url.split('/')[-1]
    urllib.urlretrieve(url, 'images/' + img_filename)


def get_page(url):
    data = urllib.urlopen(url).read()
    soup = BeautifulSoup(data)

    for item in soup.select('.item-main'):

        title = item.select('h2')[0].text.strip()

        attributes = item.select('.lwrap .attr')

        if len(attributes) < 2:
            continue

        price = attributes[0].text.strip()
        quantity = attributes[1].text.strip()

        image = item.select('.image img')[0].get('src') or item.select('.image img')[0].get('image-src')
        download_image(image)

        time.sleep(.3)

        output.append({'title': title, 'price': price, 'quantity': quantity, 'image': image})

    next_link = soup.select('a.next')

    if len(next_link) > 0:
        time.sleep(.3)
        get_page(base_url + next_link[0].get('href'))
    else:
        with open('output.json', 'w') as jsonfile:
            json.dump(output, jsonfile, indent=2)

get_page(start_url)
