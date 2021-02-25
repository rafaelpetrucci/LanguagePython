rombus = float(input())
aux = rombus
if 0 <= rombus <= 2000:
    print("Isento")
else:
    taxes = 0
    taxes1 = 1000 * 0.08
    taxes2 = 1500 * 0.18
    aux -= 2000
    if 2000 < rombus <= 3000:
        taxes = aux * 0.08
    elif 3000 < rombus <= 4500:
        aux -= 1000
        taxes = taxes1 + (aux * 0.18)
    elif rombus > 4500:
        aux -= 2500
        taxes = taxes1 + taxes2 + (aux * 0.28)
    print("R$ {:.2f}".format(taxes))
