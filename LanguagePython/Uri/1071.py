values = list()
values.append(int(input()))
values.append(int(input()))
values.sort()
count = 0
for i in range(values[0] + 1, values[1], ):
    if i % 2 == 1:
        count += i
print(count)