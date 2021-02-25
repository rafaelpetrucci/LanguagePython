i = 1
j = 7
while i <= 9 and j >= 5:
    print("I={} J={}".format(i, j))
    if j == 5:
        j = 8
        i += 2
    j -= 1