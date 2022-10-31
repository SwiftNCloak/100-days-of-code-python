print("Welcome to the tip calculator!")
totalBill = float(input("What is the total bill amount? \n$: "))
tip = int(input("How much tip would you like to give? \nPercent: "))
peopleSplit = int(input("How many people to split the bill? \nPeople: "))

calcAns = ("{:.2f}".format((((totalBill * (tip / 100)) + totalBill) / peopleSplit)))
print(f"Each person should pay: ${calcAns}")