total = 0
count = 0
average = 0
while True:
    number = input("Enter a number:")
    try:
        if number == "done":
            break
        total += float(number)
        count += 1
        average = total / count
    except:
        print("Invalid input")
print("total:", total, "count:", count, "average:", average)

# += operator lets you add two values together and assign the resultant value to a variable.
# This operator is often referred to as the addition assignment operator.
