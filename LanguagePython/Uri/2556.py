while True:
    try:
        n = int(input())
        m = input().split(" ")
        for i in range(len(m)):
            m[i] = int(m[i])
        m.sort()
        pessoas = n//2
        tempo = m[pessoas] - m[pessoas - 1]
        print("{} {}".format(pessoas, tempo))
    except EOFError:
        break