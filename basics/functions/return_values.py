#Defining functions
def sum_weights (Beep,Bop) :
  total = Bop + Beep
  return total

def calc_avg_weight (Beep,Bop):
  average= (Beep+Bop)/2
  return average

def run () :
#Asking user for input 
  print("What is the weight of Beep ?")
  Beep=float (input())
  print("What is the weight of Bop ?")
  Bop= float (input())
  print("What would like to calculate (sum or average ?")
  answer=input()
#Checking statement
  if answer == "sum" :
    action= sum_weights (Beep,Bop)
    print("The sum of Beep and Bop is {:.2f} ".format(action))
  elif answer == "average" :
    action=calc_avg_weight (Beep,Bop)
    print("The sum of Beep and Bop is {:.2f} ".format(action))
  else :
    print("You choosed wrong action")

run()