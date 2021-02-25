a, b, c = map(float, input().split())
pi = 3.14159
triangulo = (a * c)/2
circulo = pi * c **2
trapezio = ((a+b) * c)/2
quadrado = b * b
retangulo = a * b
print("TRIANGULO: {:.3f}\nCIRCULO: {:.3f}\nTRAPEZIO: {:.3f}\nQUADRADO: {:.3f}\nRETANGULO: {:.3f}".format(triangulo, circulo, trapezio, quadrado, retangulo))