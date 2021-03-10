print ("How many rows should I have ?")
row = int(input())
print ("How many columns should I have ?")
col = int(input())

for rows in range (0,row,1) :
  for cols in range (0,col,1) :
    print (" : - )", end="")
  print ()