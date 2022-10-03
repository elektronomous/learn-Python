print("Welcome to the tip calculator");

bill = float(input("What was the total bill? $"));
tipPercentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
nPersons = int(input("How many people to split the bill? "))

totalBill = (bill * (tipPercentage/100)) + bill;
personPay = totalBill / nPersons;

print(f"Each person should pay: ${round(personPay, 2)}")