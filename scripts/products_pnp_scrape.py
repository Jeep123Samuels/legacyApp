import json

import requests
from bs4 import BeautifulSoup

PAGE_SIZE = 72
PAGES = 174
BASE_URL = (
    f'https://www.pnp.co.za/pnpstorefront/pnp/en/All-Products/c/pnpbase?q=%3Arelevance&pageSize={PAGE_SIZE}'
)

products: list = list()

for x in range(0, PAGES):
    page_str: str = f'&pages={x}'
    response = requests.get(f'{BASE_URL}{page_str}')
    soup = BeautifulSoup(response.content, 'html.parser')
    results = soup.find_all('div', class_='item js-product-card-item product-card-grid')

    for elem in results:
        product_name = elem.find('div', class_='item-name')
        product_img = elem.find('img', alt=product_name.text)
        products.append(dict(img_url=product_img.attrs.get('src', ''), name=product_name.text))


with open('data.json', 'w') as f:
    json.dump(products, f)
