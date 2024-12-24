import requests
from bs4 import BeautifulSoup
import time

components_links = set()


def read_and_process_file(input_file_name, output_file_name):
    # Множество для хранения уникальных слов
    unique_words = set()

    with open(input_file_name, 'r') as input_file:
        lines = input_file.readlines()
        for line in lines:
            # Разделяем строку по первой точке и берем вторую часть
            cleaned_line = line.split('.', 1)[0].strip()
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
