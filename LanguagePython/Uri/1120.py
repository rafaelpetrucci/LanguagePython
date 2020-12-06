while True:
    string1 = input().split(" ")
    if string1[0] == string1[1] == '0':
        break
    string2 = string1[1].replace(string1[0], '')
    if string2 == "":
        string2 = "0"
    string2 = int(string2)
    print(string2)