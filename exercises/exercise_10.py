a = float(input("Enter in the angle : "))
hours = a/30
hours2 = a//30

mins = hours - hours2
mins_degree = (mins * 60) * 6 

print(float(mins_degree))