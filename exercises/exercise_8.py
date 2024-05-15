#sorted_list = []

#sorted_list.append (int(input("Enter an integer : ")))
#sorted_list.append (int(input("Enter an integer : ")))
#sorted_list.append (int(input("Enter an integer : ")))

#sorted_list.sort()

#print(sorted_list)


a = int(input())
b = int(input())
c = int(input())


min_value = a * (a <= b and a <= c) + b * (b < a or b < c) + c * (c < a and c < b)
max_value = a * (a >= b and a >= c) + b * (b > a or b > c) + c * (c > a and c > b)
mid_value = a + b + c - min_value - max_value

print(min_value)
print(mid_value)
print(max_value)
