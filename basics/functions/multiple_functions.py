def display_ladder (steps):
  #Display how many times ladder should appear
  for step in range (steps) :
    print("|   |")
    print(" *** ")
    print("|   |")


def create_ladder () :
  print( "How many steps remain ?")
  steps=int (input())
  display_ladder (steps)

create_ladder ()