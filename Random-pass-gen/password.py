import random

# Get user input
length = int(input("Enter the desired password length: "))
use_letters = input("Include letters? (yes/no): ").lower() == "yes"
use_numbers = input("Include numbers? (yes/no): ").lower() == "yes"
use_symbols = input("Include symbols? (yes/no): ").lower() == "yes"

# Build the character set based on user preferences
characters = ""
if use_letters:
    characters += "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
if use_numbers:
    characters += "0123456789"
if use_symbols:
    characters += "!@#$%^&*()_+-=[]{}|;:',.<>/?"

# Ensure at least one character type is selected
if characters == "":
    print("You must select at least one character type!")
else:
    # Generate the password
    password = ""
    for i in range(length):
        password += random.choice(characters)
    
    # Print the generated password
    print("Generated password:", password)

