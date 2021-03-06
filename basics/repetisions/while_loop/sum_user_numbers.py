print ("How many numbers I should sum up ?")
numbers= int(input())
counter= 0
final= 0

while (counter <numbers) :
  print ("Please enter the number ", counter , "of", numbers, ":")
  number=int (input())
  final=final + number
  counter=counter +1

print ("The answer is",final)