print ("How many live cables must I avoid ?")
avoid= int (input())
track= 1

while (track -1<avoid) :
  print("Avoiding...", end="")
  track=track+1
  print("Done {} live cables avoided!".format (track))
  
print ("\nAll cables have been avoided")