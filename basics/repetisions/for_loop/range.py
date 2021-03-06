print ("What level of brightness is required?")
level=int (input())

print( "Adjusting brightness...")

for brightness in range (2,level +1,2) :
  print("Beep's britghtness level:", "*" * brightness)
  print("Bop's brightness level:", "*" * brightness)
  print("\n")

print("Adjustments complete!")