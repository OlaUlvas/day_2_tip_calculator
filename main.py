

bill = float(input("How much was the bill?: "))
how_much_tip = int(input("What percentage do you want to tip the waitress?: "))
people = int(input("How many are you?: "))
the_tip = how_much_tip * 0.01 * bill
pay = bill + the_tip
to_pay_for_each = round(pay / people, 2)

print(f"Everyone has to pay ${to_pay_for_each} each.")