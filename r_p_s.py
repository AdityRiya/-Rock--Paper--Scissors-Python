import random
user_wins = 0
computer_wins = 0
options=["rock","paper","scissor"]
print(options[0])
while True:
    user_input = input("Type Rock / Paper / Scissor or 'q' to quit the game. ").lower()
    # print(user_input)
    # quit()
    if user_input == "q":
        break
    if user_input not in options:
        continue
    
    random_number = random.randint(0,2)
    computer_picks = options[random_number]
    print("Computer picks: " ,computer_picks +".")
    if user_input == "rock" and computer_picks == "scissor":
        print("You won!")
        user_wins += 1
    elif user_input == "paper" and computer_picks == "rock":
        print("You won!")
        user_wins += 1
    elif user_input == "scissor" and computer_picks == "paper":
        print("You won!")
        user_wins += 1
    else:
        print("You Loss!")
        computer_wins += 1
    


print("Scores:")
print("Your Score: ",user_wins)
print("Computer Score: ",computer_wins)
print("code is working fine.")