number = int(input())
experiment = {"C": 0, "R": 0, "S": 0, "Total": 0}
for i in range(number):
    animals = input().upper().split()
    experiment[animals[1]] += int(animals[0])
    experiment["Total"] += int(animals[0])
percent_C = (experiment["C"] * 100)/experiment["Total"]
percent_R = (experiment["R"] * 100)/experiment["Total"]
percent_S = (experiment["S"] * 100)/experiment["Total"]

print("Total: {} cobaias\nTotal de coelhos: {}\nTotal de ratos: {}\nTotal de sapos: {}\n"
      "Percentual de coelhos: {:.2f} %\nPercentual de ratos: {:.2f} %\n"
      "Percentual de sapos: {:.2f} %".format(experiment["Total"], experiment["C"], experiment["R"], experiment["S"], percent_C, percent_R, percent_S))