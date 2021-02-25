n = list(map(int, input().split()))
aux = n.copy()
n.sort()
for i in n:
    print(i)
print()
for j in aux:
    print(j)
