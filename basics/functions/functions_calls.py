#Define functions
def display_box(word):
  num_dashes = 4 + len(word)
  print("-" * num_dashes)
  print("| {} |".format(word))
  print("-" * num_dashes)

def lower_case (word) :
  print(word.lower())

def upper_case (word) :
  print(word.upper())

def display_mirror (word):
    phrase= ""
    for letter in reversed(word) :
      phrase = phrase + letter 
    print ("{}|{}:".format(word,phrase))

def display_repeated(word):
    print("How many times should the word be displayed?")
    repetitions = int(input())

    for repetition in range(repetitions):
        # even repetition
        if (repetition % 2 == 0):
            print(lower_case(word))
        # odd repetition
        else:
            print(upper_case(word))

def run () :
  print(" Please enter your name")
  word= input()
  response=0


  while (response != 6):
      #define menu

    print("What would you like to do with this word?")
    print(" -1 Display in a box")
    print(" -2 Display lower-case")
    print(" -3 Display upper-case")
    print(" -4 Display mirrored")
    print(" -5 Display repeated")
    print(" -6 Quit")
    response=int (input())

         # determine action for the menu
    if (response == 1):
          display_box(word)
    elif (response == 2):
          lower_case(word)
    elif (response == 3):
          upper_case(word)
    elif (response == 4):
          display_mirror(word)
    elif (response == 5):
          display_repeated(word)
    elif (response == 6):
        print("Thank You for using program")
        break
    else:
            print("Unknown option.") 

run()
        

