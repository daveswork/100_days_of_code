print("Welcome to the tip calculator!")
total_bill = float(input("What is the total bill? "))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

per_person = round(((total_bill * (1 + tip/100))/people),2)

print(f"Each person should pay: ${per_person:.2f}")
