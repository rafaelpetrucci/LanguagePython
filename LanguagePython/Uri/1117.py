media = []
while True:
    score = float(input())
    if 0 <= score <= 10:
        media.append(score)
        total = len(media)
        if total == 2:
            print("media = {:.2f}".format(sum(media)/total))
            break
    else:
        print("nota invalida")
