import random

word_list = [ "aardvark", "baboon", "camel" ]


chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = [ "_" for letter in chosen_word ]

print("".join(placeholder))

while "_" in placeholder:
    guess = input("Guess a letter: ").lower()
    placeholder_position = 0
    for letter in chosen_word:
        if guess == letter:
            placeholder[placeholder_position] = guess
        placeholder_position += 1
    print("".join(placeholder))