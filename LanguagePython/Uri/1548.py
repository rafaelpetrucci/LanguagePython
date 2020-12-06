n = int(input())
ordem = list()
for i in range(n):
    m = int(input())
    troca = 0
    p = input().split(" ")
    for j in range(len(p)):
        p[j] = int(p[j])
    ordem = p.copy()
    ordem.sort(reverse=True)
    for j in range(m):
        if ordem[j] == p[j]:
            troca += 1
    print(troca)