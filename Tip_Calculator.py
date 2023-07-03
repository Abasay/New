import math
print("Welcome to the tip calculator.")

totalBill = float(input("What was the total bill? $"))
def new():
    pass

percent = int(
    input("What percentage tip would you like to give? 10, 12, or 15? "))
realPercent = percent / 100
splitBill = int(input("How many people to split the bill? "))

totalBill_with_tax = totalBill + (totalBill * realPercent)

payPerPerson = totalBill_with_tax / splitBill

print("Each person should pay: $", round(payPerPerson, 2))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
