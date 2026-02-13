print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

# total_bill = (bill * tip/100) + bill
# each_person = round(total_bill / people, 2)

each_person = round((bill * (1 + tip/100)) / people, 2)

print(f"Each person should pay: $ {each_person}")
