print("Where should i look ?")
where=input()

if where == "in the bedroom" :
  print("Where in the bedroom I should look ?")
  place=input()

  if place == "under the bed" :
    print("Found some shoes but no battery")
  else:
      print("Found some mess but no battery.")

if where == "in the bathroom" :
  print("Where in the bathroom should I look?")
  bath= input()
  
  if bath == "bathtub" :
    print("Found a rubber duck but no battery")
  else :
    print("Found a wet surface but no battery")

if where == "in the lab" :
  print("Where in the lab should i look ?")
  lab = input ()

  if lab == "on the table" :
    print("Yes ! I found my battery !")
  else :
    print("I do not know where that is but I will keep looking")

       
