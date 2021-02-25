value = int(input())
print(value)
notesB = [100, 50, 20, 10, 5, 2, 1]

for i in notesB:
    notes = value // i
    print("{} nota(s) de R$ {},00".format(notes, i))
    value %= i