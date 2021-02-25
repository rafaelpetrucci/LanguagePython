days = int(input())
year = days // 365
days %= 365
month = days // 30
days %= 30
print("{} ano(s)\n{} mes(es)\n{} dia(s)".format(year,month, days))