import sys
import random
from enum import Enum

class PCB(Enum):
    Physics = 1
    Chemistry = 2
    Biology = 3
    
Playagain = True
while Playagain:
    
    studentChoice = input("\nEnter....\n1 for physics or \n2 for chemistry or \n3 for Biology\n\n")
    student = int(studentChoice)
    if student <1 or student >3:
        sys.exit("You must enter 1,2 or 3")

    

    computerChoice = random.choice("123")
    computer = int(computerChoice)
    

    print("\nYou chose " + str(PCB(student)).replace("PCB.", '') )
    print("Python chose " +str(PCB(computer)).replace("PCB.", '') )

    if student == 1 and computer == 3:
        print('\n🎉You win')
    elif student == 2 and computer == 1:
        print('\n🎉You win')
    elif student == 3 and computer == 1:
        print('\n🎉You win')
    elif student == computer:
        print("\n🙄Tie play")
    else:
        print("\n🐍Python wins")
    Playagain = input("\nPlay again?\nY for Yes\nQ for Quit\n\n")
    if Playagain.lower() == "y":
        continue
    else:
        print("\n🎉🎉🎉🎉")
        print("Thanks for Playing!")
    Playagain = False
sys.exit("\nGoodBye👋")