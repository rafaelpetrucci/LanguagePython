information = [0]*2
for i in range(1, 101):
    number = int(input())
    if number > information[0]:
        information[0] = number
        information[1] = i
print("{}\n{}".format(information[0], information[1]))