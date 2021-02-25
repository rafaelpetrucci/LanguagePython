a, b, c = map(float, input().split())
if a == 0:
    print("Impossivel calcular")
else:
    delt = b**2 - 4 * a * c
    if delt < 0:
        print("Impossivel calcular")
    else:
        r1 = (-b + (delt**(1/2)))/(2*a)
        r2 = (-b - (delt**(1/2)))/(2*a)
        print("R1 = {:.5f}\nR2 = {:.5f}".format(r1,r2))