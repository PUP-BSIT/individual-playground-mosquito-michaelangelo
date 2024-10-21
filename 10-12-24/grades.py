grade = int(input("Enter your grade: "))

if grade > 96:
    print("1.0")
elif grade <= 96 and grade >= 94:
    print("1.25")
elif grade <= 93 and grade >= 91:
    print("1.5")
elif grade <= 90 and grade >= 89:
    print("1.75")
elif grade <= 88 and grade >= 86:
    print("2.0")
elif grade <= 85 and grade >= 83:
    print("2.25")
elif grade <= 82 and grade >= 80:
    print("2.50")
elif grade <= 77 and grade >= 79:
    print("1.75")
elif grade <= 75 and grade >= 76:
    print("3.00")
elif grade < 74:
    print("5.00")