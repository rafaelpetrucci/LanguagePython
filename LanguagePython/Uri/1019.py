seconds = int(input())
minutes = seconds // 60
seconds -= minutes * 60
hour = minutes // 60
minutes -= hour * 60
print("{}:{}:{}".format(hour, minutes, seconds))