import random

def gameWin(comp , you):
    if comp == you:
        return print("Tie!")
    elif comp == 's':
        if you == 'w':
            return print("Computer wins!")
        elif you == 'g':
            return print("You win!")
    elif comp == 'w':
        if you == 'g':
            return print("Computer wins!")
        elif you == 's':
            return print("You win!")
    elif comp == 'g':
        if you == 's':
            return print("Computer wins!")
        elif you == 'w':
            return print("You win!")
        
            

print("Computer Turn : Snake(s) Water(w) or Gun(g) ? ")

#randint generates a random number from 1 to 3
randNo = random.randint(1,3)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'

you = input("Your Turn : Snake(s) Water(w) or Gun(g) ? ")

if(you == 's' or you == 'w' or you == 'g'):
    print("Computer choose : " , comp)
    print("You choose : " , you)
    gameWin(comp , you)
else:
    print("Invalid input!")
    exit()


