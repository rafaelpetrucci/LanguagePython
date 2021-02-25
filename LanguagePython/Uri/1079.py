number = int(input())
weigth = [2, 3, 5]
for i in range(number):
    average = list(map(float, input().split()))
    total = ((average[0] * weigth[0]) + (average[1] * weigth[1]) + (average[2] * weigth[2])) / sum(weigth)
    print("{:.1f}".format(total))

