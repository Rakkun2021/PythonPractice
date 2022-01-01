name = input("Enter your name\n")
print("Hello", (name))


#program to prompt the user for hours and rate per hours to compute gross pay
#1st get the inputs then specify the data type of the input values through output variable
hours = input("Enter your hours - ")
rate = input("Enter the rate - ")
pay = int(hours)*int(rate)
print(pay)