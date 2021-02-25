number = int(input())
for i in range(number):
    value = int(input())
    if value == 0:
        print("NULL")
        continue
    elif value < 0:
        if value % 2 == 0:
            print("EVEN NEGATIVE")
        else:
            print("ODD NEGATIVE")
    elif value > 0:
        if value % 2 == 0:
            print("EVEN POSITIVE")
        else:
            print("ODD POSITIVE")
