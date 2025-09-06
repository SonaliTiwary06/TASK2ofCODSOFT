#import random module
import random

#create subjects
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
special_character = ["@", "#", "$", "_"]
alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
             "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
ALPHABETS = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
             "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

# combine all characters into one pool
all_characters = numbers + special_character + alphabets + ALPHABETS

print("Welcome to the Password Generator! ")

# Step 1: User input for password length
length = int(input("Enter the desired password length: "))

# Step 2: Start the password generation loop
while True:
    # generate password of desired length
    password = ""
    for _ in range(length):
        password += random.choice(all_characters)

    print("\nYour generated password is:\n" + password)

    # ask user if they want another
    user_input = input("\nDo you want another password? (yes/no): ").strip().lower()
    if user_input == "no":
        break

#print goodbye msg
print("\nThanks for using the Password Generator. Have a fun day 🎉")
