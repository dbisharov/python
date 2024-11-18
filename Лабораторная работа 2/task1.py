money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
kol_m=0
rost=0

while True:
    rost += spend * increase
    dolg = spend + rost - salary
    if (money_capital-dolg) > 0:
        money_capital -= dolg
        kol_m += 1
    else:
        break
print("Количество месяцев, которое можно протянуть без долгов:", kol_m)
