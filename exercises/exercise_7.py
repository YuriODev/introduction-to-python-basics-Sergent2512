number = int(input("Enter 4 digit number : ")) #2804

thousands = (number // 1000)
hundreds = (number % 1000) //100
tens = (number % 100) // 10
ones = (number % 10)

print("Total sum of the digits : ", thousands + hundreds + tens + ones )