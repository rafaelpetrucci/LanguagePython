sides = list(map(float, input().split()))
sides.sort(reverse=True)
if sides[0] >= (sides[1]+sides[2]):
    print("NAO FORMA TRIANGULO")
else:
    if sides[0]**2 == (sides[1]**2 + sides[2]**2):
        print("TRIANGULO RETANGULO")
    if sides[0]**2 > (sides[1]**2 + sides[2]**2):
        print("TRIANGULO OBTUSANGULO")
    if sides[0]**2 < (sides[1]**2 + sides[2]**2):
        print("TRIANGULO ACUTANGULO")
    if sides[0] == sides[1] == sides[2]:
        print("TRIANGULO EQUILATERO")
    if sides[0] == sides[1] != sides[2] or sides[0] == sides[2] != sides[1] or sides[1] == sides[2] != sides[0]:
        print("TRIANGULO ISOSCELES")
