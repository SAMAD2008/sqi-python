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
    populations = []
    max_population = 0
    min_population = float('inf')
    max_population_country = ''
    min_population_country = ''
    total_population = 0
    density_list = []
    capitals_starting_with_a = []
    large_area_countries = []
    small_area_countries = []
    zero_population_country = ''
    for country in countries:
        name = country.find('h3', class_='country-name').get_text()
        population = int(country.find('span', class_='country-population').get_text().replace(',', ''))
        area = float(country.find('span', class_='country-area').get_text().replace(',', ''))
        capital = country.find('span', class_='country-capital').get_text()
        
        populations.append(population)
        total_population += population
        
        if population > max_population:
            max_population = population
            max_population_country = name
        if population < min_population:
            min_population = population
            min_population_country = name
        
        density = population / area if area > 0 else 0
        density_list.append((name, density))
        
        if capital.startswith('A'):
            capitals_starting_with_a.append((name, capital))
        
        if area > 1_000_000:
            large_area_countries.append(name)
        if area < 500:
            small_area_countries.append(name)
        
        if population == 0:
            zero_population_country = name
    average_population = total_population / len(countries)
    print(f'Country with the largest population: {max_population_country} ({max_population})')
    print(f'Country with the smallest population: {min_population_country} ({min_population})')
    
    

    
