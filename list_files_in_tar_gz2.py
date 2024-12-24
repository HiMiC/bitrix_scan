import tarfile
import json
import os

def get_tar_gz_files(directory):
    tar_gz_files = []

    # Проходим по всем файлам в указанной директории
    for filename in os.listdir(directory):
        # Проверяем, является ли файл .tar.gz
        if filename.endswith('.tar.gz'):
            tar_gz_files.append(os.path.join(directory, filename))

    return tar_gz_files


def list_files_in_tar_gz(tar_gz_file):
    try:
        with tarfile.open(tar_gz_file, 'r:gz') as tar:
            # Получаем список имен файлов в архиве
            file_list = tar.getnames()
            return file_list
    except Exception as e:
        print(f"Ошибка при открытии {tar_gz_file}: {e}")
        return []

def save_to_json(file_list, json_file):
    try:
        with open(json_file, 'w') as f:
            json.dump(file_list, f, indent=4)  # Сохраняем с отступами для удобства чтения
        print(f"Список файлов сохранен в {json_file}")
    except Exception as e:
        print(f"Ошибка при сохранении в {json_file}: {e}")



# Пример использования
uploads_directory = 'uploads'  # Папка, в которой нужно искать файлы
uploads_sources_directory_list = 'uploads_sources_list'  # Папка для распаковки

# Создаем папку, если она не существует
os.makedirs(uploads_sources_directory_list, exist_ok=True)

# Получаем список файлов .tar.gz
tar_gz_files = get_tar_gz_files(uploads_directory)


# Выводим найденные файлы
print("Найденные файлы .tar.gz:")
for file_path in tar_gz_files:
    print(file_path)
    # Пример использования
    #tar_gz_file_path = 'uploads/start_encode.tar.gz'  # Укажите путь к вашему файлу .tar.gz
    file_name2 = os.path.splitext(os.path.basename(file_path))[0]
    file_name = os.path.splitext(os.path.basename(file_name2))[0]

    json_file_path = uploads_sources_directory_list + '/' +file_name + '.json'  # Укажите путь к выходному JSON-файлу
    files = list_files_in_tar_gz(file_path)
    print ("Фаилов:" + str(len(files)))
    # Сохраняем список файлов в JSON-файл
    save_to_json(files, json_file_path)
