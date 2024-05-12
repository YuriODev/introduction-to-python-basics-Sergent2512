hours = int(input("Value between 0 <= h <= 12 : "))
minutes = int(input("Value between 0 <= m <= 60 : "))
seconds = int(input("Value between 0<= s <= 60 : "))

total_mins = (hours * 60) + minutes + (seconds/60)
degrees = (((total_mins * 6 ) / 360) / 12) * 360

print(degrees, "°")