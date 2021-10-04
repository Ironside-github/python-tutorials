#Snake Water & Gun Game/////RockPaper& Scissor

import random #(library file used to select a random value from a given set)

def gamewin(comp,you):
    if comp=="S" and you =="S":
        print("Its a tie. Please select again!"+"computer selects :"+str(comp) +"\n You selects:"+ str(you))
    elif comp=="S" and you=="W":
        print("You win.\n"+ "computer selects :"+str(comp) +"\n You selects:"+ str(you))
    elif comp=="S" and you=="G":
        print("You win.\n"+ "computer selects :"+str(comp) +"\n You selects:"+ str(you))
    elif comp=="W" and you=="S":
        print("Computer win.\n"+ "computer selects :"+str(comp) +"\n You selects:"+ str(you))
    elif comp=="W" and you=="W":
        print("Its a tie. Please select again!"+"computer selects :"+str(comp) +"\n You selects:"+ str(you))
    elif comp=="W" and you=="G":
        print("Computer win.\n"+ "computer selects :"+str(comp) +"\n You selects:"+ str(you))
    elif comp=="G" and you=="S":
        print("Computer win.\n"+ "computer selects :"+str(comp) +"\n You selects:"+ str(you))
    elif comp=="G" and you=="W":
        print("You win.\n"+ "computer selects :"+str(comp) +"\n You selects:"+ str(you))
    elif comp=="G" and you=="G":
        print("Its a tie. Please select again!"+"computer selects :"+str(comp) +"\n You selects:"+ str(you))
    #else:
      #  print("Please check options and select again.")
    return()



comp =print("Computer turn :Select a choice among S(snake) W(water) & G(Gun):")

randomno = random.randint(1,2)
print(randomno)
if randomno==0:
    comp== "S" 
elif randomno==1: 
    comp== "W"
elif randomno== 2:
    comp =="G"
print(comp)

you = input("Your turn: Select a choice among S(snake) W(water) & G(Gun):")
print(comp)
print(you)
gamewin(comp,you)

