number = ''
add_number = 0
while number != 0:
   number = int(input("Enter a number: "))
   if number == 0 :
      break
   add_number += number

print(f"Sum: {add_number}")