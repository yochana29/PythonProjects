import random
# Array of lowercase letters
lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
                     'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Array of uppercase letters
uppercase_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
                     'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# Array of numbers from 0 to 9
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Array of common symbols
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', 
           ']', '{', '}', ';', ':', "'", '"', ',', '<', '.', '>', '/', '?', '|', '\\']
num_lowercase = int(input("How many lowercase letters? "))
num_uppercase = int(input("How many uppercase letters? "))
num_numbers = int(input("How many numbers? "))
num_symbols = int(input("How many symbols? "))

# Create the password by combining the different character types randomly
Password=[]
for char in range (0,num_lowercase):
    Password.append(random.choice(lowercase_letters))
for char in range(0,num_uppercase):
    Password.append(random.choice(uppercase_letters))
for char in range (0,num_numbers):
    Password.append(random.choice(numbers))
for char in range(0,num_symbols):
    Password.append(random.choice(symbols))

# Shuffle the characters to ensure randomness
random.shuffle(Password)

#convert the password to a string
Password="".join(Password)
print(Password)
