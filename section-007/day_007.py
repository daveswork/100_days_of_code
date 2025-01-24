import random

word_list = [ "aardvark", "baboon", "camel" ]


chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = [ "_" for letter in chosen_word ]

print("".join(placeholder))

lives = 6

while "_" in placeholder and lives != 0:
    guess = input("Guess a letter: ").lower()
    placeholder_position = 0
    if guess in chosen_word:
        for letter in chosen_word:
            if guess == letter:
                placeholder[placeholder_position] = guess
            placeholder_position += 1
    else:
        print(f"Lives left: {lives - 1}")
        lives -= 1
    print("".join(placeholder))

if lives == 0:
    print("You lose.")
else:
    print("Congratulations!")