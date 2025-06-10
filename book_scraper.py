import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_books(url):
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    data = []
    for book in soup.select('article.product_pod'):
        title = book.h3.a['title']
        price = book.select_one('p.price_color').text
        avail = book.select_one('p.instock.availability').text.strip()
        data.append({'Title': title, 'Price': price, 'Availability': avail})
    return pd.DataFrame(data)

if __name__ == "__main__":
    URL = 'http://books.toscrape.com/'
    df = scrape_books(URL)
    df.to_csv('books.csv', index=False)
    print(df.head())
