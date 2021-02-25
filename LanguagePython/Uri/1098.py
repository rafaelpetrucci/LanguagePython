i = 0.0
j = 1.0
while i <= 2.0:
    if i == int(i):
        print("I={:.0f} J={:.0f}".format(i, j))
    else:
        print("I={} J={}".format(i, j))
    if round(j - i, 1) == 3.0:
        i = round(i + 0.2, 1)
        j = round(j - 3.0, 1)
        j = round(j + 0.2, 1)
    j = round(j + 1.0, 1)
