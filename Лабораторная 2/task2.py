salary = 5000
spend = 6000
months = 10
increase = 0.03
money_capital = 0
for month in range(months):
    ost = spend - salary
    if ost > 0:
        money_capital += ost
    spend *= (1 + increase)
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money_capital))
