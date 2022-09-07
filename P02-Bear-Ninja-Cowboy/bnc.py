
#Greeting Message
print(f"\nGet ready to play Bear, Ninja, Cowboy!\n")

#Ask user if they need instruction and Instruction message 
instructions = input("Would you like instructions? (yes/no) >" )
if instructions == "yes":
    print("\nBear, Ninja, Cowboy is an exciting game of strategy and skill! Pit your wit against the computer! Choose a player: Bear, Ninja, or Cowboy. The computer chooses a player. Bear eats Ninja, Ninja defeats Cowboy and cowboy shoots bear.\n")   
# Import the random library
# Generate a random number hence randint to pick a random element from the array
from random import randint

roles = ["Bear", "Ninja", "Cowboy"]

#capitalize first letter to avoid error if the user inputs in lowercase
computer = roles[randint(0,2)].capitalize()

player = False

while player == False:
    while True:
    # Get player input
        player = input("Bear, Ninja, or Cowboy? > ").capitalize()
        if player not in ("Bear, Ninja, Cowboy"):
            print(f"{player} is not Bear, Cowboy, or Ninja. Bear, Cowboy, and Ninja are the only allowed names.")
        else:
            break
    # Compare computer and player role
    if computer == player:
        print("DRAW!")
    elif computer == "Cowboy":
        if player == "Bear":
            print("You lose!", computer, "shoots", player)
        else: # computer is cowboy, player is ninja
            print("You win!", player, "defeats", computer)
    elif computer == "Bear":
        if player == "Cowboy":
            print("You win!", player, "shoots", computer)
        else: # computer is bear, player is ninja
            print("You lose!", computer, "eats", player)
    elif computer == "Ninja":
        if player == "Cowboy":
            print("You lose!", computer, "defeats", player)
        else: # computer is ninja, player is bear
            print("You win!", player, "eats", computer)
    #prompt user if they want to play again.
    play_again = input("\nWould you like to play again? (yes/no) > ")
    if play_again == 'yes':
        player = False
        computer = roles[randint(0,2)]
    else: #end game
        break


