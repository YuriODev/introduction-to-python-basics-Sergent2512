denominations = [500, 100, 10, 5, 2, 1] # 2804
s = int(input("Enter the value of your shopping $ : "))

for denomination in denominations:
    number = s// denomination
    print("The number of", denomination , "bills needed is :" , number)
    s %= denomination