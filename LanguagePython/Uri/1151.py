n = int(input())
primeiro = 0
segundo = 1
terceiro = primeiro + segundo
for c in range(n):
    if c < n - 1:
        print(primeiro, end=' ')
        primeiro = segundo
        segundo = terceiro
        terceiro = primeiro + segundo
    else:
        print(primeiro)