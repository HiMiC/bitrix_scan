import tarfile
import json
import os


def get_tar_gz_files(directory):
    tar_gz_files = []
    for filename in os.listdir(directory):
        tar_gz_files.append(os.path.join(directory, filename))
    return tar_gz_files




def save_to_json(file_list, json_file):
    try:
        with open(json_file, 'w') as f:
            json.dump(file_list, f, indent=4)
        print(f"Список файлов сохранен в {json_file}")
    except Exception as e:
        print(f"Ошибка при сохранении в {json_file}: {e}")


def compare_json_files(json_file1, json_file2):
    try:
        # Загружаем данные из JSON-файлов
        with open(json_file1) as f1, open(json_file2) as f2:
            data1 = json.load(f1)
            data2 = json.load(f2)

            # Преобразуем списки в множества для удобного сравнения
            set1 = set(data1)
            set2 = set(data2)

            # Находим элементы, которые есть только в первом и только во втором файле
            only_in_file1 = set1 - set2
            only_in_file2 = set2 - set1

            return only_in_file1, only_in_file2
    except Exception as e:
        print(f"Ошибка при сравнении файлов: {e}")
        return None, None


# Пример использования
uploads_sources_directory_list = 'uploads_sources_list'

os.makedirs(uploads_sources_directory_list, exist_ok=True)

# Получаем список файлов .tar.gz
tar_gz_files = get_tar_gz_files(uploads_sources_directory_list)

# Выводим найденные файлы и обрабатываем их
print(tar_gz_files)

# Пример сравнения двух JSON-файлов
if len(tar_gz_files) >= 2:
    json_file1 = tar_gz_files[0]
    print(json_file1)
    json_file2 = tar_gz_files[1]
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
