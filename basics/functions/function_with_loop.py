def cross_bridge (steps):
  for distance in range (steps):
    print("Crossed step")
  
  if steps>5 :
      print("The bridge is colapsing")
  else:
      print ("We must keep going")

cross_bridge (3)
cross_bridge (6)