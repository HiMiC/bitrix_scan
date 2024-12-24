import json


def extract_modules_from_file(file_path):
    modules = set()  # Используем множество для уникальных значений
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()  # Убираем пробелы и символы новой строки
                if line:  # Проверяем, что строка не пустая
                    parts = line.split('/')
                    if len(parts) > 3:  # Проверяем, что путь содержит модуль
                        module_name = parts[3]  # Модуль находится на третьем уровне
                        modules.add(module_name)
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

    return list(modules)  # Преобразуем множество обратно в список


# Путь к файлу, содержащему пути к модулям
input_file = 'modules.txt'  # Замените на имя вашего файла

# Извлекаем модули
modules = extract_modules_from_file(input_file)

print("всего модулей: "+str(len(modules)))

# Сохраняем в JSON-файл
output_file = 'modules.json'
with open(output_file, 'w') as f:
    json.dump(modules, f, indent=4)

print(f"Модули сохранены в файл {output_file}: {modules}")


