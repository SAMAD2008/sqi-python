# Go to https://www.scrapethissite.com/pages/simple/.
# Count how many countries are listed on the page.
# Print the country with the largest and smallest population.
# Calculate the average population of all countries.
# For each country, compute its population density (people per km²): density = population / area. List the top 3 countries with the highest density.
# Find all countries whose capital city starts with the letter "A". Return Xa list of those countries and their capitals.
# Find countries with an area greater than 1,000,000 km²
# Find countries with an area less than 500 km²
# Get the country that has 0 population.
import requests
from bs4 import BeautifulSoup
url = 'https://www.scrapethissite.com/pages/simple/'
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    countries = soup.find_all('div', class_='country')
    print(f'Total number of countries: {len(countries)}')
  
    
    

    
