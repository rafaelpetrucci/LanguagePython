start_Day = int(input().replace("Dia", "").replace(" ", ""))
start_Hour = list(map(int, input().replace(":", "").split()))
seconds_Initial = (start_Hour[0]*3600) + (start_Hour[1]*60) + start_Hour[2]

end_Day = int(input().replace("Dia", "").replace(" ", ""))
end_Hour = list(map(int, input().replace(":", "").split()))
sum_Days = end_Day - start_Day
seconds_End = (sum_Days *86400) + (end_Hour[0] * 3600) + (end_Hour[1] * 60) + end_Hour[2]

seconds_Total = seconds_End - seconds_Initial
day = seconds_Total // 86400
seconds_Total %= 86400
hour = seconds_Total // 3600
seconds_Total %= 3600
minutes = seconds_Total // 60
seconds_Total %= 60
seconds = seconds_Total
print('{} dia(s)'.format(day))
print('{} hora(s)'.format(hour))
print('{} minuto(s)'.format(minutes))
print('{} segundo(s)'.format(seconds))
