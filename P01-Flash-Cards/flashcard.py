import json
#open the file and parse the JSON into python library
#Python dictionary keys have `''` single quotes and Jason keys have double quotes `""`. 

with open('me-capitals.json', 'r') as f:
    data = json.load(f)

#defined variable named score to track scores
#total is length of card array
total = len(data["cards"])

#while loop to get the player to input play again once the game ends

player = False

while player == False:
    score = 0

#We access the ["cards"] key, to get back its array value
# added for loop iterator to iterate over all the cards
#now use the 'input' function to prompt the user to enter an input.
#check the user input for correct answeres and display "Correct!" or "Incorrect!"
#to improve the user experience, added the correct answer when the answer is incorrect.
    for i in data["cards"]:
        guess = input(i["q"] + " >")

#add string function to make the answer lowercase to tackle case sesitive error in answers
        if guess.lower() == i["a"].lower():
            #add (**increment**) 1 to score
            score += 1
            # interpolate score and total into the response
            print(f"\nCorrect! Current score: {score}/{total}\n")
            
        else:
            print(f"Incorrect! The correct answer was", i["a"])
            print(f"\nCurrent Score: {score}/{total}\n")
    
    #print total score when the game ends
    print(f"\nThanks for Playing. Your Total Score is {score}/{total}.")
    
    #assigned a variable half_total to get half of the total answers
    half_total = total / 2
    if score < half_total:
        print("\nYou just need a little bit practice.\n")
    elif score > half_total:
        print("\nGreat. You are good at this.\n")
    elif score == total:
        print("\nAmazing. You are a genious.\n")

    #while loop to ask user to input yes or no and break if the imput is no. 
    play_again = input("Do you want to play again? Enter yes or no\n")
    if play_again.lower() == "yes":
        player == False
        print("\nHere you go!")
    else:
        print("\nSee you later!")
        break
