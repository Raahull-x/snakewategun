import random
computer = random.choice([-1,0,1])
youstr = input("Enter your choice ").lower()
youDict = {
    "s": 1, #snake
    "w": -1, #water
    "g": 0 # gun
}

reverseDict = {
    1: "Snake",
    0: "Gun",
    -1: "Water"
}

if youstr not in youDict:
    print("Invalid choice! Please choose 's', 'w', or 'g'.")
else:
    you = youDict[youstr]

    print(f"You chose {reverseDict[you]}")
    print(f"Computer chose {reverseDict[computer]}")

    # Determine the winner based on game rules
    if computer == you:
        print("It's a tie!")
    elif (you == 1 and computer == -1) or (you == -1 and computer == 0) or (you == 0 and computer == 1):
        # (Snake beats Water) or (Water beats Gun) or (Gun beats Snake)
        print("You win!")
    else:
        print("You lose!")




#         Step 1: Importing the random Module
# python
# Copy code
# import random
# The random module is imported to generate random choices for the computer. This adds an element of unpredictability to the game, making it more fun.
# Step 2: Computer Makes a Random Choice
# python
# Copy code
# computer = random.choice([-1, 0, 1])
# random.choice([-1, 0, 1]) randomly selects a value from the list [-1, 0, 1].
# In this game:
# -1 represents "Water"
# 0 represents "Gun"
# 1 represents "Snake"
# This line simulates the computer's random choice in the game.
# Step 3: Prompting the User for Their Choice
# python
# Copy code
# youstr = input("Enter your choice ").lower()
# This line takes input from the user and converts it to lowercase using .lower().
# The user is expected to enter 's' for Snake, 'w' for Water, or 'g' for Gun.
# Step 4: Creating Dictionaries for Mapping Choices
# python
# Copy code
# youDict = {
#     "s": 1,  # 's' for Snake
#     "w": -1, # 'w' for Water
#     "g": 0   # 'g' for Gun
# }

# reverseDict = {
#     1: "Snake",
#     0: "Gun",
#     -1: "Water"
# }
# youDict: Maps user input ('s', 'w', 'g') to corresponding numerical values:
# 's' maps to 1 (Snake)
# 'w' maps to -1 (Water)
# 'g' maps to 0 (Gun)
# reverseDict: Maps numerical values back to their string representation:
# 1 maps to "Snake"
# 0 maps to "Gun"
# -1 maps to "Water"
# Step 5: Validating User Input
# python
# Copy code
# if youstr not in youDict:
#     print("Invalid choice! Please choose 's', 'w', or 'g'.")
# This condition checks if the user's input (youstr) is a valid key in youDict.
# If the input is not 's', 'w', or 'g', it prints an error message and stops further execution.
# Step 6: Mapping User Input to Game Choice
# python
# Copy code
# else:
#     you = youDict[youstr]
# If the user's input is valid, it maps the input to its numerical value using youDict.
# you now holds a numerical value (1, 0, or -1) representing the user's choice.
# Step 7: Displaying Choices
# python
# Copy code
# print(f"You chose {reverseDict[you]}")
# print(f"Computer chose {reverseDict[computer]}")
# Uses reverseDict to convert the numerical values back into their string representations.
# Displays both the user's and the computer's choices.
# Step 8: Determining the Game Outcome
# python
# Copy code
# if computer == you:
#     print("It's a tie!")
# First, it checks if the user's choice is the same as the computer's choice.
# If they are equal, the game is a tie.
# Step 9: Checking Winning Conditions
# python
# Copy code
# elif (you == 1 and computer == -1) or (you == -1 and computer == 0) or (you == 0 and computer == 1):
#     # (Snake beats Water) or (Water beats Gun) or (Gun beats Snake)
#     print("You win!")
# This line checks the winning conditions:
# (you == 1 and computer == -1): Snake (1) beats Water (-1).
# (you == -1 and computer == 0): Water (-1) beats Gun (0).
# (you == 0 and computer == 1): Gun (0) beats Snake (1).
# If any of these conditions are true, the user wins.
# Step 10: Remaining Condition - The User Loses
# python
# Copy code
# else:
#     print("You lose!")
# If it's not a tie and none of the winning conditions are met, then the user loses.
# Summary
# The computer makes a random choice between Snake, Water, and Gun.
# The user is prompted to make their choice.
# The game checks if the input is valid.
# It compares the user's choice with the computer's choice using the game's rules.
# The game announces the result (tie, win, or lose) based on the choices.