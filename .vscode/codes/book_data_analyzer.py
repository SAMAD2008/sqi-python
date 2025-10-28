import requests
from bs4 import BeautifulSoup

data = requests.get('http://books.toscrape.com')

soup = BeautifulSoup(data.content, 'html.parser')

all_books = soup.find_all('article')

print("The total number of books are: ", len(all_books))


all_prices = []
max_book_price = 0
max_book_data = {

}
for book in all_books:

    price_string = book.find('p', class_='price_color').get_text()

    book_h3 = book.find('h3')
    price = float(price_string[1:])
    if price > max_book_price:
        max_book_price = price
        
        max_book_data['name'] =  book_h3.find('a')['title']
        max_book_data['price'] =  price
     
    all_prices.append(price)

print(sum(all_prices) / len(all_prices))

print("Info of book with the maximum data: ", max_book_data)


