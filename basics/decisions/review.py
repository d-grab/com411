print ("What did You eat today?")
meal =input()
print ("It was nice ?")
it =input()
print ("Where did You go ?")
go =input()

if ((meal == "ham") and (it == "yes") and (go== "walk")) :
  print("That was nice food !, good that You went for a walk")
  
elif ((meal== "pizza") and (it== "yes") or (it=="no")and (go=="home")) :
    print( "Wow i wish to eat pizza and stay home \n Did you play any games ?")
    games =input()
    if games== "yes" :
      print ("Call me I will play with You")
    else:
      print("At least you had nice food ")

elif ((meal == "chicken") or (it== "yes") or (go== "nowhere")) :
  print ("Looks like You had fun today")

else :
  print("Now it's time to relax and play some games :)")

