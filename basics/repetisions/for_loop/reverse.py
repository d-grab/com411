print ("What phrase do You see ?")
word=input()

print("Reversing ...")

for invert in range(len(word)-1,-1,-1):
  print ("The phrase is :",word[invert])