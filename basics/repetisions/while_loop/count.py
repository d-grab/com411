print ("How many live cables must I avoid ?")
avoid= int (input())
track= 1

while (track -1<avoid) :
  print("Avoiding...", end="")
  print("Done {} live cables avoided!".format (track))
  track=track+1
  
print ("\nAll cables have been avoided")