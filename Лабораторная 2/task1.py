money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
months = 0
total_money = money_capital
while (total_money + salary) >= spend:
    total_money += salary
    total_money -= spend
    months += 1
    spend *= (1 + increase)
print("Количество месяцев, которое можно протянуть без долгов:", months)
