#If the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
bill =float(input("what was the total bill?"))
tip =float(input("what percentage tip would you like to give? 10, 12 or 15?"))
numPeople = int(input("how many people to split the bill?"))
totalBill = bill*(1 + tip/100)
eachPays = round(totalBill/numPeople, 2)
finalAmount= "{:.2f}".format(eachPays)

print(f"Each person should pay ${finalAmount}")