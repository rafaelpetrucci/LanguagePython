while True:
    try:
        pe = dict()
        temporaria = list()
        count = par = 0
        n = int(input())
        while count < n:
            string = str(input()).strip().upper()
            sapato = string.split(' ')
            if pe.get(sapato[0]) is None:
                temporaria.append(sapato[1])
                pe[sapato[0]] = temporaria.copy()
                temporaria.clear()
            elif sapato[1] in pe[sapato[0]]:
                pe[sapato[0]].append(sapato[1])
            elif sapato[1] not in pe[sapato[0]]:
                par += 1
                pe[sapato[0]].pop(0)
                if len(pe[sapato[0]]) == 0:
                    pe.pop(sapato[0], None)
            count += 1
        print(par)
    except EOFError:
        break
