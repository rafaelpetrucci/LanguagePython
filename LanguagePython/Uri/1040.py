n1, n2, n3, n4 = map(float, input().split())
media = (n1*2 + n2*3 + n3*4 + n4)/(2+3+4+1)
if media >= 7.0:
    print("Media: {:.1f}\nAluno aprovado.".format(media))
elif media < 5.0:
    print("Media: {:.1f}\nAluno reprovado.".format(media))
else:
    print("Media: {:.1f}\nAluno em exame.".format(media))
    exame = float(input())
    print("Nota do exame: {:.1f}".format(exame))
    media = (media + exame)/2
    if media >= 5.0:
        print("Aluno aprovado.")
    elif media < 5.0:
        print("Aluno reprovado")
    print("Media final: {:.1f}".format(media))