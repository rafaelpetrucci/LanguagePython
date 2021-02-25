salary = float(input())
percent = 0
if 0 <= salary <= 400:
    percent = 15
elif 400 < salary <= 800:
    percent = 12
elif 800 < salary <= 1200:
    percent = 10
elif 1200 < salary <= 2000:
    percent = 7
elif salary > 2000:
    percent = 4
earned = salary * (percent / 100)
new_Salary = salary + earned
print("Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: {} %".format(new_Salary, earned, percent))