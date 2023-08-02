def dividing(price, percent, people_number):
    tip_as_percent = percent / 100
    total_tip_ammount = price * tip_as_percent
    total_bill = price + total_tip_ammount
    bill_per_preson = total_bill / people_number
    print(f"Each person should pay:{bill_per_preson} zł")


print("Welcome to Tip Calculator")
price = int(input("What was the total bill?\n"))
percent = int(input("What percentage tip would you like to give? 10, 12, or 15 \n"))
people_number = int(input("How many people to split the bill?\n"))

dividing(price, percent, people_number)
