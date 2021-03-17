
def menu():
  print("\nWhat would You like to do ?")
  print(" \n 1- Load Data\n 2- Process Data\n 3- Visualise Data\n 4- Save Data\n 5- Exit  ")
  option = int(input())
  if option == 1:
    return option
  if option == 2:
      return option
  if option == 3:
      return option
  if option == 4:
      return option
  if option == 5:
      return option
  else:
      print("Invalid selection")
      return


def started (operation):
    operation = menu()
    if operation <= 4 :
      #IS that ok format for message ?
        print(f"{operation} A string indicating the operation being started ") 
    if operation == 1 :
      # Or that one is correct ?
      print (f"{operation} Loading data has started ") 

#When I add menu() program will run twice ? but i can not pass the operation parameter to started ( .. ) like started (operation)
started(menu)