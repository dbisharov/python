salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

rost=0
money_capital=0
for i in range(1, months, 1):
    rost += spend * increase
    dolg = spend + rost - salary
    money_capital += dolg
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", int(money_capital))
