while True:
    points = list(map(int, input().split()))
    if points[0] == 0 or points[1] == 0:
        break
    if points[0] > 0 and points[1] > 0:
        print("primeiro")
    elif points[0] > 0 and points[1] < 0:
        print("quarto")
    elif points[0] < 0 and points[1] > 0:
        print("segundo")
    elif points[0] < 0 and points[1] < 0:
        print("terceiro")