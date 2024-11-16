import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    """Читает CSV, конвертирует в JSON и сохраняет в файл с отступами."""
    with open(INPUT_FILENAME, 'r', encoding='utf-8') as f:
        lines = [row for row in csv.DictReader(f)]  # Читаем строки как словари

    with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as f:
        json.dump(lines, f, indent=4, ensure_ascii=False)  # Сохраняем в JSON


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
