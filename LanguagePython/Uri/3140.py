valor = 0
while True:
    try:
        html = input()
        if valor > 0:
            if "</body>" in html:
                valor = 0
                continue
            print(html)
        if "<body>" in html:
            valor = 1
    except EOFError:
        break