import tarfile
import json
import os


def get_tar_gz_files(directory):
    tar_gz_files = []
    for filename in os.listdir(directory):
        if filename.endswith('.tar.gz'):
            tar_gz_files.append(os.path.join(directory, filename))
    return tar_gz_files


def list_php_files_in_tar_gz(tar_gz_file):
    php_files = []
    try:
        with tarfile.open(tar_gz_file, 'r:gz') as tar:
            for member in tar.getmembers():
                if member.name.endswith('.php'):
                    php_files.append(member.name)
            return php_files
    except Exception as e:
        print(f"Ошибка при открытии {tar_gz_file}: {e}")
        return []


def save_to_json(file_list, json_file):
    try:
        with open(json_file, 'w') as f:
            json.dump(file_list, f, indent=4)
        print(f"Список файлов сохранен в {json_file}")
    except Exception as e:
        print(f"Ошибка при сохранении в {json_file}: {e}")


def compare_json_files(json_file1, json_file2):
    try:
        with open(json_file1) as f1, open(json_file2) as f2:
            data1 = json.load(f1)
            data2 = json.load(f2)
            return data1 == data2
    except Exception as e:
        print(f"Ошибка при сравнении файлов: {e}")
        return False


# Пример использования
uploads_directory = 'uploads'
uploads_sources_directory_list = 'uploads_sources_list'

os.makedirs(uploads_sources_directory_list, exist_ok=True)

# Получаем список файлов .tar.gz
tar_gz_files = get_tar_gz_files(uploads_directory)

# Выводим найденные файлы и обрабатываем их
print("Найденные файлы .tar.gz:")
for file_path in tar_gz_files:
    print(file_path)

    # Извлекаем имя файла без расширения
    file_name2 = os.path.splitext(os.path.basename(file_path))[0]
    file_name = os.path.splitext(os.path.basename(file_name2))[0]

    json_file_path = os.path.join(uploads_sources_directory_list, f'{file_name}.json')

    # Получаем список PHP-файлов из архива и сохраняем в JSON
    php_files = list_php_files_in_tar_gz(file_path)
    print ("Фаилов:" + str(len(php_files)))
    save_to_json(php_files, json_file_path)

# Пример сравнения двух JSON-файлов
if len(tar_gz_files) >= 2:
    json_file1 = os.path.join(uploads_sources_directory_list,
                              os.path.splitext(os.path.splitext(os.path.basename(tar_gz_files[0]))[0])[0] + '.json')
    print(json_file1)
    json_file2 = os.path.join(uploads_sources_directory_list,
                              os.path.splitext(os.path.splitext(os.path.basename(tar_gz_files[1]))[0])[0] + '.json')
    print(json_file2)
    only_in_file1, only_in_file2 = compare_json_files(json_file1, json_file2)

    if only_in_file1 is None and only_in_file2 is None:
        print("Не удалось сравнить файлы.")
    else:
        if not only_in_file1 and not only_in_file2:
            print(f"{json_file1} и {json_file2} равны.")
        else:
            if only_in_file1:
                print(f"Файлы, присутствующие только в {json_file1}:")
                for item in only_in_file1:
                    print(item)
            if only_in_file2:
                print(f"Файлы, присутствующие только в {json_file2}:")
                for item in only_in_file2:
                    print(item)
else:
    print("Недостаточно файлов .tar.gz для сравнения.")
