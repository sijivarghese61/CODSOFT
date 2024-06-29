#--------------------------------Rock-Paper-Scissors Game---------------------------

import random
count_w=0
total_g=0
#----> Adding Random choice for System

def comp():
    lists=["Rock","Paper","Scissors"]
    return random.choice(lists)

#----> Taking Player's choice

def game():
    computer=comp()
    option=input("Choose Rock, Paper or Scissors (Enter R/P/S) OR enter Q to QUIT the Game: ").upper()
    if(option=='R'):
        player="Rock"
    elif(option=='P'):
        player="Paper"
    elif(option=='S'):
        player="Scissors"
    elif(option=='Q'):
        exit()
    else:
        print("Invalid Input. Try Again!")
        game()
    global total_g
    total_g+=1
    check(player,computer)

#----> Checking for the Result and printing it

def check(p,c):
    print(f"System's choice: {c}\nPlayer's choice: {p}")
    if(c==p):
        opt=input("It's a TIE.\nDo you wish to play again (Enter Y or N): ").upper()
        if(opt=='Y'):
            game()
        else:
            exit()
    elif((c=='Scissors'and p=='Paper')or(c=='Paper'and p=='Rock')or(c=='Rock'and p=='Scissors')):
        opt=input("YOU LOSE :(\nDo you wish to play again (Enter Y or N): ").upper()
        if(opt=='Y'):
            game()
        else:
            exit()
    else:
        global count_w,total_g
        count_w+=1
        print(f"Congrats! YOU WIN :)\nTotal WINS: {count_w}/{total_g}")
        opt=input("Do you wish to play again (Enter Y or N): ").upper()
        if(opt=='Y'):
            game()
        else:
            exit()


#----> Starting of the game and Instructions

print("Welcome!\nTo Rock Paper Scissors Game.")
print("""GAME INSTRUCTIONS:
    •Scissors beats Paper
    •Paper beats Rock
    •Rock beats Scissors
Let The Game Begin!""")
while True:
    game()
