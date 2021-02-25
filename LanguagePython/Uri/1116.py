number = int(input())
for i in range(number):
    dividing = list(map(int, input().split()))
    if dividing[1] == 0:
        print("divisao impossivel")
        continue
    print("{:.1f}".format(dividing[0]/dividing[1]))