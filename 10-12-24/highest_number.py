number_1 = int(input("Enter 1st number: "))
number_2 = int(input("Enter 2nd number: "))
number_3 = int(input("Enter 3rd number: "))

if number_1 > number_2 and number_1 > number_3:
    print("The largest number is the 1st number")
elif number_2 > number_1 and number_2>  number_3:
    print("The largest number is the 2nd number")
else:
    print("The largest number is the 3rd number")