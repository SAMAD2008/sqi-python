# Scrape (the first page of) quotes from the site and perform some basic text and author-based analysis.
# Use the demo site: http://quotes.toscrape.com/
# Count total number of quotes
# Count the number of unique authors
# Find the author with the most quotes on the page
# Count how many quotes contain the word “is” (case-insensitive)
# List all tags that appear and how many times each appears
import requests
from bs4 import BeautifulSoup
url = 'http://quotes.toscrape.com/'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    quotes = soup.find_all('div', class_='quote')
    print(f'Total number of quotes: {len(quotes)}')

is_word_count = 0
tag_count = {}
for quote in quotes:
    text = quote.find('span', class_='text').get_text()
    author = quote.find('small', class_='author').get_text()
    tags = [tag.get_text() for tag in quote.find_all('a', class_='tag')]
    
    if 'is' in text.lower():
        is_word_count += 1
   
    for tag in tags:
        tag_count[tag] = tag_count.get(tag, 0) + 1

print(f'Number of quotes containing the word "is": {is_word_count}')








