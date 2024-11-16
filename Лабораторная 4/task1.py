"""
Модуль для расчета суммы произведений значений "score" и "weight" в JSON-файле.
"""

import json

INPUT_FILE = "input.json"


def task() -> float:
    """Читает JSON-файл и возвращает сумму произведений 'score' и 'weight', округленную до 3 знаков."""
    with open(INPUT_FILE, 'r') as f:
        json_data = json.load(f)

    sum_values = sum(item.get("score", 0) * item.get("weight", 0) for item in json_data)
    return round(sum_values, 3)


print(task())
