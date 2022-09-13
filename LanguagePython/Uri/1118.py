media = []
count = 0
while True:
    total = len(media)
    if total == 2:
        if count == 2:
            count = 0
            print('media = {:.2f}'.format(sum(media) / 2))
        test = input('novo calculo (1-sim 2-nao)\n')
        if test == '1':
            media = []
        elif test == '2':
            break
    else:
        number = float(input())
        if 0 <= number <= 10:
            media.append(number)
            count += 1
        else:
            print('nota invalida')
