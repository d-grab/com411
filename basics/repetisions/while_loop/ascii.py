print ("How many bars should be charged ?")
bars = int (input())
track = 0

while ( track<bars) :
  track= track +1
  print("Charging:", "\t█" * track)
  
print ("Battery fully charged")