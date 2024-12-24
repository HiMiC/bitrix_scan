import requests
from bs4 import BeautifulSoup
import time

components_links = set()

def parse_bitrix_marketplace(url, start_page, end_page):
    for page in range(int(start_page), int(end_page) + 1):
        time.sleep(3)
        # Формируем URL для текущей страницы
        page_url = f"{url}&PAGEN_1={page}"
        print(f"Парсинг страницы: {page_url}")
        # Отправляем GET запрос
        response = requests.get(page_url)
        # Проверяем успешность запроса
        if response.status_code == 200:
            # Парсим HTML контент
            soup = BeautifulSoup(response.content, 'html.parser')
            # Находим все элементы решений
            solutions = soup.find_all('span', class_='item-wrap')
            for solution in solutions:
                # Извлекаем ссылку на решение
                link = solution.find('a', href=True)['href']
                # Удаляем /solutions/ и /
                cleaned_link = link.replace('/solutions/', '').replace('/', '')
                components_links.add(cleaned_link)
                #print(f'Link: {cleaned_link}')
                #print('-' * 40)
        else:
            print(f'Не удалось получить страницу. Код состояния: {response.status_code}')

def save_links_to_file(links, file_name):
    with open(file_name, 'w') as file:
        for link in links:
            file.write(f"{link}\n")

def get_last_page_number(base_url):
    response = requests.get(base_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        navigation_pages = soup.find('div', class_='navigation-pages')
        if navigation_pages:
            # Найти все ссылки с классом "nav-page"
            page_links = navigation_pages.find_all('a', class_='nav-page')
            if page_links:
                # Получить номер последней страницы из последнего элемента
                last_page_link = page_links[-1]
                last_page_url = last_page_link.get('href')
                # Извлечь номер страницы из URL
                last_page_number = last_page_url.split('PAGEN_1=')[-1]
                return last_page_number
            else:
                print("Не найдено страниц для навигации.")
                return None
        else:
            print("Не найден блок навигации страниц.")
            return None
    else:
        print(f"Ошибка при запросе страницы. Код состояния: {response.status_code}")
        return None

# URL-ы страниц решений 1C-Битрикс Маркетплейс
urls = [
    'https://marketplace.1c-bitrix.ru/solutions/?category=&PAYMENT_SHOW=ALL&INSTALLS_CNT=%D0%9D%D0%B5+%D0%B2%D0%B0%D0%B6%D0%BD%D0%BE',
    'https://marketplace.1c-bitrix.ru/solutions/?category=&PAYMENT_SHOW=NOT_FREE&INSTALLS_CNT=%D0%9D%D0%B5+%D0%B2%D0%B0%D0%B6%D0%BD%D0%BE',
    'https://marketplace.1c-bitrix.ru/solutions/?category=&PAYMENT_SHOW=FREE&INSTALLS_CNT=%D0%9D%D0%B5+%D0%B2%D0%B0%D0%B6%D0%BD%D0%BE',
    'https://marketplace.1c-bitrix.ru/solutions/?category=&PAYMENT_SHOW=ACTION&INSTALLS_CNT=%D0%9D%D0%B5+%D0%B2%D0%B0%D0%B6%D0%BD%D0%BE'
]

# Парсим страницы с 2 по 50 для каждого URL
for url in urls:
    # Получить номер последней страницы
    last_page_number = get_last_page_number(url)

    if last_page_number:
        print(f"Номер последней страницы: {last_page_number}")
    else:
        print("Не удалось получить номер последней страницы.")
    parse_bitrix_marketplace(url, 1, last_page_number)

# Сохраняем ссылки в файл
file_name = "bitrix_links.txt"
save_links_to_file(components_links, file_name)

print(components_links)
print("Количество: ")
print(len(components_links))

def read_and_process_file(input_file_name, output_file_name):
    # Множество для хранения уникальных слов
    unique_words = set()

    with open(input_file_name, 'r') as input_file:
        lines = input_file.readlines()
        for line in lines:
            # Разделяем строку по первой точке и берем вторую часть
            cleaned_line = line.split('.', 0)[-1].strip()
            # Добавляем очищенное слово в множество
            unique_words.add(cleaned_line)

    with open(output_file_name, 'w') as output_file:
        for word in unique_words:
            output_file.write(f"{word}\n")

    print(f"Данные успешно обработаны и сохранены в файл {output_file_name}")
    print(f"Уникальные слова: {unique_words}")
    print(f"Количество уникальных слов: {len(unique_words)}")

# Имена файлов
input_file_name = 'bitrix_links.txt'
output_file_name = 'bitrix_links_dir_razrab.txt'

# Чтение, обработка файла и сохранение уникальных слов
read_and_process_file(input_file_name, output_file_name)
