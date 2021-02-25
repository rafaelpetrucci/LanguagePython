count = 0
sum_Total = 0
for i in range(6):
    value = float(input())
    if value > 0:
        count += 1
        sum_Total += value
average = sum_Total / count
print("{} valores positivos\n{:.1f}".format(count, average))

