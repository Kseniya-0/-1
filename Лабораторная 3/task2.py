def find_common_participants(group1, group2, a=','):
    participants1 = group1.split(a)
    participants2 = group2.split(a)
    common_participants = participants1.intersection(participants2)
    common_participants_list = list(common_participants)
    common_participants_list.sort()
    return common_participants_list


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
common = find_common_participants(participants_first_group, participants_second_group, a='|')
print("Общие участники:", common)
