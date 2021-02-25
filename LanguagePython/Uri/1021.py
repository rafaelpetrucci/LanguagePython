value = float(input())
notes = [100, 50, 20, 10, 5, 2]
coins = [1.00, 0.50, 0.25, 0.10, 0.05, 0.01]
print("NOTAS:")
for i in notes:
    note = int(value / i)
    print("{} nota(s) de R$ {}.00".format(note, i))
    value %= i
print("MOEDAS:")
for i in coins:
    coin = int(value / i)
    print("{} moeda(s) de R$ {:.2f}".format(coin, i))
    value = round(value % i, 2)