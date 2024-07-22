#!/bin/bash

# Проверка, что переданы два аргумента
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 input_path output_path"
    exit 1
fi

input_path=$1
output_path=$2

# Создание виртуальной среды
python -m venv venv

# Активация виртуальной среды
source venv/Scripts/activate

# Обновление pip
pip install --upgrade pip
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118
# Установка необходимых библиотек из requirements.txt
pip install -r requirements.txt

# Запуск Python скрипта main.py с передачей аргументов
python main.py "$input_path" "$output_path"

# Деактивация виртуальной среды
deactivate
