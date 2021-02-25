def absolute(a):
    if a > 0:
        return a
    else:
        return a * -1


a, b, c = map(int, input().split())
maior = int((a + b + absolute(a - b))/2)
maior = int((maior + c + absolute(maior - c))/2)
print("{} eh o maior".format(maior))
