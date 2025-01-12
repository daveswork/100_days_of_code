import random

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

computer_choice = random.randint(0,2)

choices = ["Rock", "Paper", "Scissors"]

print(f"You picked {choices[user_choice]}")
print(f"The computer picked {choices[computer_choice]}")

if user_choice == computer_choice:
    print("It's a Draw!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif user_choice == 1 and computer_choice == 0:
    print("You win!")
elif user_choice == 2 and computer_choice == 1:
    print("You win!")
else:
    print("You lose.")
