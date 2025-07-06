import sys
import random

def Guess (name = 'Player1' ):
    GameCount = 0
    PlayerWins = 0
    
    def GuessNumber():
        nonlocal name 
        nonlocal PlayerWins
        
        UserChoice = input(
            f"{name} \n Try to guess the number i am thinking of.... beween (1 and 5) "
        )
        if UserChoice not in ['1','2','3','4','5']:
            print(f"{name} Please enter between  1 and 5")
            return GuessNumber()
    
       
        computerChoice = random.choice("12345")
        
    

        print(f" \n {name}You chose {UserChoice}"  )
        print(f"I was thinking about {computerChoice} "  )
        
        User = int(UserChoice)
        computer = int(computerChoice)
        
        def Who_Wins(User, computer):
            nonlocal name
            nonlocal PlayerWins
            
            if User == computer:
                PlayerWins +=1
                return f"{name} You won!"
            else:
                return f"{name} Try again!"
            
        game_results = Who_Wins(User, computer)
        print(game_results)
        
        nonlocal GameCount
        GameCount += 1
        
        print(f"\n Game Counts {GameCount} \n")
        print(f"\n{name}'s wins: {PlayerWins}")
        print(f"\n {name} Your Winning Percentage is: {PlayerWins/GameCount}:.2%")
        print(f"\nPlay again? {name}!")
         
        while True:
            PlayAgain = input("\nY for Yes \n Q to Quit")
            if PlayAgain.lower() not in ["y","q"]:
                continue
            else:
                break
        if PlayAgain.lower() == "y":
            return GuessNumber
        else:
            print("\n🎉🎉🎉🎉")
            print("Thanks for Playing!")
            Playagain = False
            if __name__ == "__main__":
                sys.exit("\nGoodBye👋")
            else:
                return
    return GuessNumber
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description= "provide a personaized game experience."
    )
    parser.add_argument(
        "_n", '__name', metavar ='name',
        required=True, help = "The name of the person Playing the game."
    )
    args = parser.parse_args()
    Guess_my_number = Guess(args.name)
    Guess_my_number()
        
        
   