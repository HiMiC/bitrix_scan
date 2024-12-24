import requests
import json
import os

# Список URL файлов
urls = [
    "https://www.1c-bitrix.ru/download/files/start_encode.tar.gz",
    "https://www.1c-bitrix.ru/download/files/standard_encode.tar.gz",
    "https://www.1c-bitrix.ru/download/files/small_business_encode.tar.gz",
    "https://www.1c-bitrix.ru/download/files/business_encode.tar.gz",
    "https://www.1c-bitrix.ru/download/files/portal/bitrix24_shop_encode.tar.gz",
    "https://www.1c-bitrix.ru/download/files/business_cluster_postgresql_encode.tar.gz"
]

# Папка для загрузки файлов
download_folder = 'uploads'

# Создаем папку, если она не существует
os.makedirs(download_folder, exist_ok=True)


# Функция для получения размера файла
def get_file_size(url):
    try:
        response = requests.head(url)
        if response.status_code == 200:
            file_size = response.headers.get('Content-Length')
            if file_size:
                return int(file_size)  # Возвращаем размер в байтах
            else:
                return None
        else:
            print(f"Ошибка при получении файла {url}: {response.status_code}")
            return None
    except Exception as e:
        print(f"Произошла ошибка при обработке {url}: {e}")
        return None


# Функция для загрузки файла
def download_file(url):
    local_filename = os.path.join(download_folder, url.split('/')[-1])

    # Проверяем, существует ли локальный файл и его размер
    if os.path.exists(local_filename):
        local_file_size = os.path.getsize(local_filename)
        print(f"Локальный файл {local_filename} уже существует, его размер: {local_file_size} байт.")

        # Получаем размер файла на сервере
        remote_file_size = get_file_size(url)
        if remote_file_size is not None:
            if local_file_size == remote_file_size:
                print(f"Размеры совпадают. Файл {local_filename} не будет загружен.")
                return True  # Файл не будет загружен, так как размеры совпадают

    try:
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(local_filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
        print(f"Файл загружен: {local_filename}")
        return True  # Успешная загрузка
    except Exception as e:
        print(f"Ошибка при загрузке файла {url}: {e}")
        return False  # Неудачная загрузка


# Функция для загрузки предыдущих размеров из JSON-файла
def load_previous_sizes(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as json_file:
            return json.load(json_file)
    return {}


# Функция для сохранения текущих размеров в JSON-файл
def save_current_sizes(filename, sizes):
    with open(filename, 'w') as json_file:
        json.dump(sizes, json_file, indent=4)


# Функция для записи неудачных загрузок в JSON-файл
def log_failed_downloads(filename, failed_urls):
    with open(filename, 'w') as json_file:
        json.dump(failed_urls, json_file, indent=4)


# Основной процесс
previous_sizes = load_previous_sizes('file_sizes.json')
current_sizes = {}
failed_downloads = []

# Проверяем размеры файлов и запоминаем их
for url in urls:
    size = get_file_size(url)
    if size is not None:
        current_sizes[url] = size  # Сохраняем текущий размер в байтах
        # Сравниваем с предыдущим размером
        previous_size = previous_sizes.get(url)
        if previous_size is not None:
            if size != previous_size:
                print(f"Размер файла {url} изменился: {previous_size} -> {size}")
            else:
                print(f"Размер файла {url} не изменился: {size}")
        else:
            print(f"Размер файла {url} новый: {size}")
    else:
        print(f"Не удалось получить размер файла {url}.")
# Обновляем только существующие размеры в файле
previous_sizes.update(current_sizes)

# Сохраняем обновленные размеры в JSON-файл
save_current_sizes('file_sizes.json', previous_sizes)

# Загружаем файлы и записываем неудачные загрузки
for url in current_sizes.keys():
    if current_sizes[url] != -1:  # Если размер файла успешно получен
        print(f"Попытка загрузки файла {url}...")
        if not download_file(url):  # Пытаемся скачать файл
            failed_downloads.append(url)  # Добавляем в список неудачных загрузок

# Записываем неудачные загрузки в отдельный JSON-файл
log_failed_downloads('failed_downloads.json', failed_downloads)

print("Текущие размеры файлов сохранены в 'file_sizes.json'.")
print("Неудачные загрузки записаны в 'failed_downloads.json'.")
