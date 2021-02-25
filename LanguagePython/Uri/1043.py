a,b,c = map(float, input().split())
if abs((a-b)) < c < (a+b):
    perimetro = a+b+c
    print("Perimetro = {:.1f}".format(perimetro))
else:
    area = ((a+b)*c)/2
    print("Area = {:.1f}".format(area))