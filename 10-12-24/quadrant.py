x_axis = int(input("Enter x-coordinate: "))
y_axis = int(input("Enter y-coordinate: "))

if x_axis > 0 and y_axis > 0:
    print("The coordinate is located at quadrant 1")
elif x_axis < 0 and y_axis > 0:
    print("The coordinate is located at quadrant 2")
elif x_axis < 0 and y_axis < 0:
    print("The coordinates is located at quadrant 3")
elif x_axis > 0 and y_axis < 0:
    print ("The coordinate is located at quadrant 4")
else:
    print("The coordinate is located at origin")