k = int(input())
if k == 1:
    k = 1
elif k <= 3:
    k = 3
elif k <= 5:
    k = 5
elif k <= 10:
    k = 10
elif k <= 25:
    k = 25
elif k <= 50:
    k = 50
elif k <= 100:
    k = 100
print('Top {}'.format(k))