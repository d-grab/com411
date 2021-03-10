print ("Please enter the sequence")
sequence= input()
print ("Please enter a character for the marker") 
marker= input()

marker_position1= -1
marker_position2= -1

for position in range (0, len(sequence),1) :
  letter=sequence [position]

  if (letter==marker):
    if (marker_position1== -1):
      marker_position1=position
    else:
        marker_position2=position

print (f"The distance between the markers is {marker_position2 - marker_position1 -1}.")


