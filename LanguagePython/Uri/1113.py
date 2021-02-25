while True:
    numbers = list(map(int, input().split()))
    if numbers[0] == numbers[1]:
        break
    if numbers[0] > numbers[1]:
        print("Decrescente")
    else:
        print("Crescente")