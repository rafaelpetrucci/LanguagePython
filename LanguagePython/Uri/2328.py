n = int(input())
a = input().split()
soma = 0
for i in range(n):
    a[i] = int(a[i])
for i in range(n):
    soma += (a[i] - 1)
print(soma)