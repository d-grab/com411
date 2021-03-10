print("Program started")
print("Please enter an ASCII code")
code = int (input())
#Build-in funcion abs() change negative integer to positive
code=abs(code)

#I use if statement to check if the number is in range 36-126
if code in range (36,127) :
  print ( f"The character represented by the ASCII code {code} is:",chr(code))
else:
  print("Your number is not from range 36 to 126 ! Try again")

print("\nProgram Ended !")
