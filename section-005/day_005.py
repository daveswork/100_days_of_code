import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', \
'n', 'o', 'p', 'q', 'r', 's', 't','u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C'\
'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S'\
'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

all_chars = [letters, numbers, symbols]

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

total_characters = nr_letters + nr_symbols + nr_numbers

password = ""

# password = random.sample(letters, nr_letters) + random.sample(numbers,nr_numbers) + random.sample(symbols, nr_symbols)

# random.shuffle(password)
# password = "".join(password)
# print(password)

password_list = []

for i in range(0, nr_letters):
    password_list.append(random.choice(letters))

for i in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

for i in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)

print(f"Your new password is: {''.join(password_list)}")



