epr = 1.5
hours = input("Enter hours -")
rate = input("Enter rate -")
hours = float(hours)  # we need to declare data type
rate = float(rate)  # we need to declare data type

if int(hours) <= 40:
    pay = int(hours) * int(rate)
    print("Pay -", pay)
elif int(hours) >= 40:
     pay_r = (rate * 40)
     pay_e = int(hours) - 40
     pay_f = float(pay_e * epr) * int(rate)
     pay_c = float(pay_f) + int(pay_r)
     print("Pay -", int(pay_c))
