list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]
seredina = len(list_players) // 2  # Середина списка = целое от деления количества эл-ов на два
pervaya_komanda = list_players[0:seredina]  # Имена до середины  - первая команда
vtoraya_komanda = list_players[seredina:]  # Имена с середины - вторая команда
print(pervaya_komanda)
print(vtoraya_komanda)
