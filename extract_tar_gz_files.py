import os
import tarfile



def get_tar_gz_files(directory):
    tar_gz_files = []

    # Проходим по всем файлам в указанной директории
    for filename in os.listdir(directory):
        # Проверяем, является ли файл .tar.gz
        if filename.endswith('.tar.gz'):
            tar_gz_files.append(os.path.join(directory, filename))

    return tar_gz_files


def extract_tar_gz_files(tar_gz_files, output_directory):
    for tar_gz_file in tar_gz_files:
        try:
            with tarfile.open(tar_gz_file, 'r:gz') as tar:
                tar.extractall(path=output_directory)
                print(f"Распакован: {tar_gz_file} в {output_directory}")
        except Exception as e:
            print(f"Ошибка при распаковке {tar_gz_file}: {e}")


# Пример использования
uploads_directory = 'uploads'  # Папка, в которой нужно искать файлы
uploads_sources_directory = 'uploads_sources'  # Папка для распаковки

# Создаем папку, если она не существует
os.makedirs(uploads_sources_directory, exist_ok=True)

# Получаем список файлов .tar.gz
tar_gz_files = get_tar_gz_files(uploads_directory)


# Выводим найденные файлы
print("Найденные файлы .tar.gz:")
for file in tar_gz_files:
    print(file)
    file_name2 = os.path.splitext(os.path.basename(file))[0]
    file_name = os.path.splitext(os.path.basename(file_name2))[0]
    # Создаем папку, если она не существует
    extract_dir = uploads_sources_directory+'/'+file_name
    os.makedirs(extract_dir, exist_ok=True)

    # Распаковываем найденные файлы
    print("Распаковываем в: " + extract_dir)
    extract_tar_gz_files(tar_gz_files, extract_dir)
