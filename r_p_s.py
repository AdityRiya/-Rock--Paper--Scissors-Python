import random
user_wins = 0
computer_wins = 0
while True:
    user_input = input("Type Rock / Paper / Scissor or 'q' to quit the game. ").lower()
    # print(user_input)
    # quit()
    if user_input == "q":
        break
    if user_input not in ["rock","paper","scissor"]:
        continue



print("code is working fine.")