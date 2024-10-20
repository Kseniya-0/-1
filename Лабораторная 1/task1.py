numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

summa = sum(numbers[0:numbers.index(None)])+sum(numbers[numbers.index(None)+1:])  # Сложение всех элементов кроме None
numbers[4] = summa / len(numbers)  # Замена элемента на среднее арифметическое. (кол-во элементов включает в себя None)
print("Измененный список:", numbers)
