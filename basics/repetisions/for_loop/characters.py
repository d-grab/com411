print ("What strange markings do you see ?")
markings=input()

for marks in range (0,len(markings),1) :
  print ("Index ",marks,":",(markings[marks]))

print ("Done!")