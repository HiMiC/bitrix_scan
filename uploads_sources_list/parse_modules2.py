import os
import json
from pprint import pprint

# Пример использования
uploads_sources_directory_list = '.'

def get_tar_gz_files(directory):
    tar_gz_files = []

    # Проходим по всем файлам в указанной директории
    for filename in os.listdir(directory):
        # Проверяем, является ли файл .tar.gz
        if filename.endswith('.json'):
            tar_gz_files.append(os.path.join(directory, filename))

    return tar_gz_files

def save_to_json(file_list, json_file):
    try:
        with open(json_file, 'w') as f:
            json.dump(file_list, f, indent=4)
        print(f"Список файлов сохранен в {json_file}")
    except Exception as e:
        print(f"Ошибка при сохранении в {json_file}: {e}")

def serialize_sets(obj):
    if isinstance(obj, set):
        return list(obj)

    return obj



# Получаем список файлов .tar.gz
tar_gz_files = get_tar_gz_files(uploads_sources_directory_list)




for file in tar_gz_files:
    modules = set()
    print(file)
    file_name = os.path.splitext(os.path.basename(file))[0]

    with open(file) as json_data:
        data = json.load(json_data)
        #pprint(d)
        json_data.close()
        for line in data:
            #print(line)
            line = line.strip()  # Убираем пробелы и символы новой строки
            if line:  # Проверяем, что строка не пустая
                parts = line.split('/')
                if len(parts) > 3:  # Проверяем, что путь содержит модуль
                    module_name = parts[3]  # Модуль находится на третьем уровне
                    modules.add(module_name)
    print("всего модулей: " + str(len(modules)))
    print(type(modules))
    json_str = json.dumps(modules, default=serialize_sets)
    print(json_str)

    save_to_json(json_str, "./22/modules_"+file_name+".json")
    #save_to_json(modules, "modules_"+file_name+".json")
    #for i in modules:
     #   print(i)
    print("======")

# Iterating through the json list


