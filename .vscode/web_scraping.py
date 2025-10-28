import requests
from bs4 import BeautifulSoup

# Fetch the website content using requests
url = 'https://www.example.com'  # You can change this to a URL of your choice
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the content using Beautiful Soup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract the header
    header = soup.find('h1')

    if header:
        print('Header:', header.get_text())

    # Extract the main content (assuming main content is within <main> tag or similar)
    main_content = soup.find('main')
    if main_content:
        print('Main Content:', main_content.get_text())
    else:
        # Fallback: Extract all paragraphs as main content
        paragraphs = soup.find_all('p')
        for p in paragraphs:
            print('Paragraph:', p.get_text())
else:
    print('Failed to retrieve the webpage. Status code:', response.status_code)
