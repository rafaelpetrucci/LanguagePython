start_Day = int(input().replace("Dia", "").replace(" ", ""))
start_Hour = list(map(int, input().replace(":", "").split()))
end_Day = int(input().replace("Dia", "").replace(" ", ""))
end_Hour = list(map(int, input().replace(":", "").split()))
if end_Hour[2] < start_Hour[2]:
    end_Hour[2] += 60
    start_Hour[1] += 1
if end_Hour[1] < start_Hour[1]:
    end_Hour[1] += 60
    start_Hour[0] += 1
if end_Hour[0] < start_Hour[0]:
    end_Hour[0] += 24
    start_Day += 1
second = end_Hour[2] - start_Hour[2]
minute = end_Hour[1] - start_Hour[1]
hour = end_Hour[0] - start_Hour[0]
day = end_Day - start_Day
print("{} dia(s)\n{} hora(s)\n{} minuto(s)\n{} segundo(s)".format(day, hour, minute, second))