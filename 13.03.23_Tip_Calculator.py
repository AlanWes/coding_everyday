bill = input("What was the total bill? $")
tip = input("What percentage tip would you like to give? 10, 12 or 15? ")
people = input("How many people split the bill? ")

int_bill = float(bill)
int_tip = int(tip)
int_people = int(people)

mid_tip = int_tip / 100

add_tip = int_bill * mid_tip
main_tip = int_bill + add_tip

main_bill = main_tip / int_people

total = format(main_bill, '.2f')

print(f"Each person should pay: ${total}")