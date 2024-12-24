import requests
from bs4 import BeautifulSoup

def parse_bitrix_marketplace(url):
    # Send a GET request to the URL
    response = requests.get(url)
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        #print(soup)
        # Find all solution items
        #solutions = soup.find_all('div', class_='solution-item')
        #solutions = soup.find_all('span', class_='rat_text', limit=5)

        solutions = soup.find_all('span', class_='item-wrap')
        #solutions = soup.find_all('a', class_='item-block')
        print(solutions)
        for solution in solutions:
            # Extract the solution name
            #name = solution.find('span', class_='item-name-text').get_text(strip=True)
            #print(name)
            # Extract the solution link
            link = solution.find('a', href=True)['href']
            # Extract the solution description
            #description = solution.find('div', class_='solution-item-description').get_text(strip=True)
            #print(f'Name: {name}')
            print(f'Link: {link}')
            #print(f'Description: {description}')
            print('-' * 40)
    else:
        print(f'Failed to retrieve the page. Status code: {response.status_code}')

# URL of the 1C-Bitrix marketplace solutions page
url = 'https://marketplace.1c-bitrix.ru/solutions/'
parse_bitrix_marketplace(url)


# URL страницы решений 1C-Битрикс Маркетплейс
base_url = 'https://marketplace.1c-bitrix.ru/solutions/?category=&PAYMENT_SHOW=ALL&INSTALLS_CNT=%D0%9D%D0%B5+%D0%B2%D0%B0%D0%B6%D0%BD%D0%BE'
# Парсим страницы с 2 по 50
parse_bitrix_marketplace(base_url, 1, 50)