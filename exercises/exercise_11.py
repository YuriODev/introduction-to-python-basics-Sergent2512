#denominations = [500, 100, 10, 5, 2, 1] # 2804
#s = int(input("Enter the value of your shopping $ : "))

#for denomination in denominations:
 #   number = s// denomination
  #  print("The number of", denomination , "bills needed is :" , number)
   # s %= denomination

s = int(input("Enter the value of your shopping in $ : "))

bills_500 = s // 500
s %= 500

bills_100 = s // 100
s %= 100

bills_10 = s // 10
s %= 10

bills_5 = s // 5
s %= 5

bills_1 = s

print(f"{bills_500} (500), {bills_100} (100), {bills_10} (10), {bills_5} (5), {bills_1} (1)")
