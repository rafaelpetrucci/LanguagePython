valorStr = str(input()).strip()
saltos = valorStr.split()

valor2Str = str(input()).strip()
canos = valor2Str.split()
resultado = 0
for c in range(int(saltos[1]) - 1):
    diferente = int(canos[c+1]) - int(canos[c])
    if diferente < 0:
        diferente = diferente * -1
    if int(saltos[0]) < diferente:
        resultado += 1
        break
if resultado == 0:
    print('YOU WIN')
elif resultado != 0:
    print('GAME OVER')