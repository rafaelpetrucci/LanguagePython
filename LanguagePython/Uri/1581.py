n = int(input())
for c in range(n):
    k = int(input())
    s = list()
    for i in range(k):
        s.append(input())
    s.sort()
    if s[0] == s[k-1]:
        print(s[0])
    else:
        print("ingles")