import string
import random

# Define the sets of characters to exclude
excluded_chars = string.ascii_letters + string.digits + string.whitespace
all_letters_list = list(string.ascii_letters)
numbers_only = list(string.digits)

#print ("All Letters:", all_letters_list)
#print ("Numbers Only:", numbers_only)

# Generate the non-alphabetic, non-numeric, non-whitespace characters
# by iterating through all printable characters and checking the exclusion criteria.
symbols_only = ""
for char in string.printable:
    if char not in excluded_chars:
        symbols_only += char

# Print the resulting characters (might contain some non-standard printable characters depending on locale)
#print(symbols_only)#
print(random.choice(all_letters_list))
print("Welcome to the Python Password Generator!!!")
num_letters  = int(input("How many letters would you like in your password? "))
num_symbols  = int(input(f"How many symbols would you like? "))
num_numbers  = int(input(f"How many numbers would you like?? "))
password_list = []
for char in range(1, num_letters + 1):
    password_list.append(random.choice(all_letters_list))
for char in range(1, num_symbols + 1):
    password_list.append(random.choice(symbols_only))       
for char in range(1, num_numbers + 1):
    password_list.append(random.choice(numbers_only))
random.shuffle(password_list)
password = ""
for char in password_list:
    password += char
print(f"Your password is: {password}")

# Note this needs to be called thru the vscode terminal due to docker issues with interactive setup
# docker run -it --rm -v ${PWD}:/app passwordgenerator:latest ls /app
