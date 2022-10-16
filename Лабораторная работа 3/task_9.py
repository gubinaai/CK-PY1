salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

current_spend = spend
for capital in range(1, months + 1):
    capital = (current_spend - salary)
    current_spend = current_spend * (increase + 1)
    need_money += capital

print(round(need_money))
