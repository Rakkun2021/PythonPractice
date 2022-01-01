my_list = []                        # Initialize array
while True:
    number = 0.0
    input_number = input('Enter a number: ')            #Initialize loop
    if input_number == 'done':
        break

    try:
        number = float(input_number)
    except ValueError:                        #Initialize condition
        print('Invalid input')
        quit()

    my_list.append(input_number)

if my_list:
    print('Maximum: ', max(my_list) or None)
    print('Minimum: ', min(my_list) or None)