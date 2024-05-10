n = int(input("Enter the number of seconds. : "))

hours = n // 3600

seconds_left = n % 3600

minutes = seconds_left // 60

seconds = seconds_left % 60

time = "{}:{}:{}".format(hours, minutes, seconds)

print(time)