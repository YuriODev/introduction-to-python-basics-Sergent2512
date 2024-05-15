n = int(input("Enter the number of seconds. : "))

hours = n // 3600 % 24

seconds_left = n % 3600

minutes = seconds_left // 60

seconds = seconds_left % 60

print(f"{hours}:{minutes:02d}:{seconds:02d}")
