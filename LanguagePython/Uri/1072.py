number = int(input())
count_In = count_Out = 0
for i in range(number):
    number_Test = int(input())
    if 10 <= number_Test <= 20:
        count_In += 1
    else:
        count_Out +=1
print("{} in\n{} out".format(count_In, count_Out))
