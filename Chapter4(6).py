def compute_pay():
    hours = input('Enter hours - ')
    rate = input('Enter rate - ')
    hours = float(hours)
    rate = float(rate)

    if hours >= 40:
        pay_e = hours - 40
        pay_c = (pay_e * 1.5) + 40
        pay_f = pay_c * rate
        print('Your pay is - ', pay_f)
    else:
        pay_r = hours * rate
        print('Your pay is - ', pay_r)


compute_pay()
